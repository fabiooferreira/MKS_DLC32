"""CNC_FFST HMAC v1, shared key carried inside the bundled BIN. No unsigned-motion fallback."""
import argparse
import hashlib
import hmac
import json
import math
import os
from pathlib import Path
import queue
import re
import secrets
import threading
import time

SAFE_REALTIME = {0x18, ord('?'), ord('!'), 0x80, 0x82, 0x84, 0x85, 0x87}
REALTIME_WIRE = bytes.maketrans(b'?!', b'\x80\x82')


KEY_PREFIX = b'FFST_SHAREDKEY1:'
KEY_SUFFIX = b':FFST_KEY_END'


def load_key(path=None):
    # The matching firmware BIN is bundled as EXE data, so there is no external key file.
    path = Path(path or Path(__file__).with_name('CNC_FFST_0.3.0_FULL_4MB.bin'))
    try:
        data = path.read_bytes()
        index = data.find(KEY_PREFIX)
        if index < 0 or data.find(KEY_PREFIX,index+1) >= 0:
            raise ValueError('record')
        start = index+len(KEY_PREFIX)
        key = data[start:start+32]
        if len(key)!=32 or data[start+32:start+32+len(KEY_SUFFIX)]!=KEY_SUFFIX:
            raise ValueError('record')
        return key
    except (OSError, ValueError) as exc:
        raise RuntimeError('BIN correspondente ausente/inválido. Use o pacote Python completo.') from exc


def verify_firmware(port, identity_path=None, writer=None, reader=None):
    path = Path(identity_path or Path(__file__).with_name('firmware_identity.json'))
    try:
        identity = json.loads(path.read_text(encoding='utf-8'))
        expected = identity['app_image_sha256']
        version = identity['firmware']
    except (OSError, ValueError, KeyError) as exc:
        raise RuntimeError('Manifesto do firmware ausente/inválido. Use o pacote Python completo.') from exc
    lines = exchange(port, '$FFINFO', writer=writer, reader=reader)
    if '[FFFW:' + version + ':' + expected + ']' not in lines:
        raise RuntimeError('A placa não está com o BIN CNC_FFST esperado por este programa.')
    return expected


def mac(key, message):
    return hmac.new(key, message.encode('ascii'), hashlib.sha256).hexdigest()


def exchange(port, command, timeout=8, writer=None, reader=None):
    wire = command.encode('ascii') + b'\n'
    if (writer or port.write)(wire) != len(wire):
        raise OSError('Escrita incompleta na autenticação: ' + command.split('=', 1)[0])
    lines = []
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        line = (reader or port.readline)().decode('ascii', 'replace').strip()
        if not line:
            continue
        lines.append(line)
        if line.startswith('error:'):
            if '[FFUNPAIRED]' in lines:
                raise RuntimeError('Firmware não corresponde à edição de chave fixa.')
            stage = command.split('=', 1)[0]
            raise RuntimeError(f'A placa recusou a autenticação: etapa {stage}, resposta {line}. '
                               'Confira se o BIN CNC_FFST 0.3.0 correspondente está gravado.')
        if line == 'ok':
            return lines
    stage = command.split('=', 1)[0]
    raise TimeoutError(f'A placa não respondeu na etapa {stage}. '
                       'Confira o BIN CNC_FFST 0.3.0, a porta e 115200 baud.')


class SessionChanged(RuntimeError):
    pass


class SignedPort:
    """Serial-compatible wrapper. A separate pump keeps ACK handling independent of GUI locks.

    Commands are signed individually, not unlocked globally. One envelope at a time
    prevents the ASCII HMAC overhead from overrunning the GRBL RX buffer.
    """
    def __init__(self, raw, key, boot_wait=3, identity_path=None):
        self.raw = raw
        self.key = key
        self.seq = 0
        self.rtseq = 0
        self._rt_tx = threading.Lock()
        self._wire = threading.Lock()
        self._raw_tx = threading.Lock()
        self.nonce = None
        self.failure = None
        self._closed = False
        self._responses = queue.Queue()
        self._ready = threading.Event()
        self._ready.set()
        self._tx = threading.Lock()
        self._kind = None
        self._rx_fragment = bytearray()
        self._last_line = ''
        self._pending_command = None
        self._pending_since = None
        self._pending_sequence = self._pending_tag = None
        self._receipt_query = None
        self._last_probe_at = 0
        self._ack_probe_after = 3.0
        self._ack_timeout = 120.0
        self._pending_timeout = self._ack_timeout
        self.recovered_receipts = 0
        self.last_motion_progress = 0
        self._last_status_at = 0
        self._last_machine_state = ''
        self._last_reported_position = None
        self._identity_path = identity_path
        self._recovering = False
        self._generation = 0
        try:
            time.sleep(boot_wait)
            raw.reset_input_buffer()
            self._authenticate()
        except Exception:
            raw.close()
            raise
        self._reader = threading.Thread(target=self._pump, daemon=True)
        self._reader.start()

    def _write_raw(self, data):
        # Windows pyserial uses one overlapped-write structure per port.
        # Never let status polling race a command/handshake write.
        status_only = bool(data) and all(c in (ord('?'), 0x80, 0x87) for c in data)
        if not self._raw_tx.acquire(blocking=not status_only):
            return len(data)  # A later poll will request fresh status.
        try:
            return self.raw.write(data)
        finally:
            self._raw_tx.release()

    def _read_line(self):
        # pyserial.readline() can return a fragment when its 100 ms timeout expires.
        # A fragment or empty read must never be interpreted as a complete ACK.
        if b'\n' not in self._rx_fragment:
            chunk = self.raw.readline()
            if chunk:
                self._rx_fragment.extend(chunk)
        if len(self._rx_fragment) > 65536:
            raise OSError('Resposta serial sem terminador excedeu 64 KiB; conexão interrompida.')
        if b'\n' not in self._rx_fragment:
            return b''
        end = self._rx_fragment.index(b'\n') + 1
        line = bytes(self._rx_fragment[:end])
        del self._rx_fragment[:end]
        self._last_line = line.decode('ascii', 'replace').strip()
        return line

    def communication_diagnostics(self):
        elapsed = time.monotonic() - self._pending_since if self._pending_since else 0
        return (f'Comando pendente: {self._pending_command or "—"}; '
                f'espera: {elapsed:.1f}s; sequência: {self.seq}; '
                f'última linha: {self._last_line[:180] or "—"}; '
                f'fragmento RX: {len(self._rx_fragment)} bytes; '
                f'confirmações recuperadas: {self.recovered_receipts}; '
                f'consulta ativa: {self._receipt_query is not None}')

    def _track_status(self, response):
        if not (response.startswith(b'<') and response.rstrip().endswith(b'>')):
            return
        fields = response.decode('ascii', 'replace').strip()[1:-1].split('|')
        self._last_machine_state = fields[0].split(':', 1)[0].lower()
        self._last_status_at = time.monotonic()
        for field in fields[1:]:
            if field.startswith(('MPos:', 'WPos:')):
                try:
                    name, values = field.split(':', 1)
                    position = tuple(float(value) for value in values.split(','))
                    if not position or not all(math.isfinite(value) for value in position):
                        return
                    previous = self._last_reported_position
                    if (previous is not None and previous[0] == name and previous[1] != position and
                            self._last_machine_state in ('run', 'jog', 'home', 'homing')):
                        self.last_motion_progress = self._last_status_at
                    self._last_reported_position = (name, position)
                except ValueError:
                    pass
                break

    def acknowledgement_wait_is_paused(self):
        return (self._last_machine_state in ('hold', 'door') and
                time.monotonic() - self._last_status_at < 3)

    def _ack_expired(self):
        if self.acknowledgement_wait_is_paused():
            return False
        budget = self._ack_timeout if math.isinf(self._pending_timeout) else self._pending_timeout
        activity = max(self._pending_since or 0, self.last_motion_progress)
        return time.monotonic() - activity >= budget

    def _maybe_receipt_probe(self):
        if self._recovering or not self._pending_command or not self._pending_since:
            return
        elapsed = time.monotonic() - self._pending_since
        if self._ack_expired():
            raise TimeoutError('Sem confirmação da placa. ' + self.communication_diagnostics() +
                               '. Pare e reconecte; comando não será repetido.')
        interval = min(self._ack_probe_after, self._pending_timeout / 3)
        if self._receipt_query or self._rx_fragment or elapsed < interval:
            return
        if time.monotonic() - self._last_probe_at < interval:
            return
        challenge = secrets.token_hex(16)
        self._receipt_query = {'sequence': self._pending_sequence, 'tag': self._pending_tag,
                               'nonce': self.nonce, 'generation': self._generation,
                               'challenge': challenge, 'status': None}
        self._last_probe_at = time.monotonic()
        wire = ('$FFACK=' + self._pending_sequence + ',' + challenge + '\n').encode('ascii')
        if self._write_raw(wire) != len(wire):
            raise OSError('Escrita incompleta da consulta de confirmação; comando não repetido.')

    def _consume_receipt(self, response):
        text = response.decode('ascii', 'replace').strip()
        query = self._receipt_query
        if text.startswith('[FFACK:'):
            if query is None:
                raise RuntimeError('Confirmação recebida fora de uma consulta; conexão bloqueada.')
            match = re.fullmatch(r'\[FFACK:([0-9]+):([0-9a-f]{32}):(PENDING|[0-9]+):([0-9a-f]{64})\]', text)
            if (not match or match[1] != query['sequence'] or match[2] != query['challenge'] or
                    query['nonce'] != self.nonce or query['generation'] != self._generation):
                raise RuntimeError('Identidade da confirmação inválida; comando não repetido.')
            status = match[3]
            message = 'ack|' + query['nonce'] + '|' + query['challenge'] + '|' + query['sequence'] + '|'
            message += 'PENDING' if status == 'PENDING' else query['tag'] + '|' + status
            if not hmac.compare_digest(mac(self.key, message), match[4]):
                raise RuntimeError('Prova da confirmação inválida; conexão bloqueada.')
            query['status'] = status
            return True
        if query is None or not (text == 'ok' or text.startswith('error:')):
            return False
        # During a receipt query, a bare OK could be the command's ACK OR the
        # query terminator. Quarantine it until the authenticated proof arrives.
        if query['status'] is None:
            if text.startswith('error:'):
                raise RuntimeError('Consulta de confirmação recusada: ' + text)
            return True
        if text != 'ok':
            raise RuntimeError('Consulta de confirmação não foi concluída: ' + text)
        self._receipt_query = None
        self._last_probe_at = time.monotonic()
        status = query['status']
        if status == 'PENDING':
            return True
        if (query['sequence'] != self._pending_sequence or query['tag'] != self._pending_tag or
                not self._pending_command):
            raise RuntimeError('Confirmação não corresponde ao comando pendente.')
        self._kind = None
        self._pending_command = self._pending_since = None
        self._pending_sequence = self._pending_tag = None
        self.recovered_receipts += 1
        self._responses.put(b'[MSG:Confirmacao recuperada sem reenviar comando.]\n')
        self._responses.put(b'ok\n' if int(status) == 0 else ('error:' + status + '\n').encode('ascii'))
        self._ready.set()
        return True

    def _authenticate(self):
        image_hash = verify_firmware(self.raw, self._identity_path, writer=self._write_raw, reader=self._read_line)
        lines = exchange(self.raw, '$FFHELLO', writer=self._write_raw, reader=self._read_line)
        matches = [re.fullmatch(r'\[FFNONCE:([0-9a-f]{64}):([0-9a-f]{64})\]', s)
                   for s in lines]
        match = next((m for m in matches if m), None)
        if not match:
            raise RuntimeError('Resposta de autenticação inválida.')
        self.nonce = match[1]
        if not hmac.compare_digest(mac(self.key, 'server|' + self.nonce + '|' + image_hash), match[2]):
            raise RuntimeError('A placa não corresponde à chave local.')
        reply = exchange(self.raw, '$FFAUTH=' + mac(self.key, 'client|' + self.nonce + '|' + image_hash), writer=self._write_raw, reader=self._read_line)
        if '[FFAUTH:OK]' not in reply:
            raise RuntimeError('Autenticação não confirmada.')
        self.seq = self.rtseq = 0

    @property
    def authenticated(self):
        return self.is_open and self.nonce is not None and not self._recovering and self.failure is None

    def _recover_session(self):
        self._recovering = True
        self._ready.clear()
        self._generation += 1
        pending, self._kind = self._kind, None
        try:
            with self._wire:
                time.sleep(.2)
                self.raw.reset_input_buffer()
                self._rx_fragment.clear()
                self._pending_command = self._pending_since = None
                self._pending_sequence = self._pending_tag = None
                self._receipt_query = None
                self._authenticate()
            self.failure = None
            if pending is not None:
                # Stop the application's outstanding operation. Never repeat an uncertain move.
                self._responses.put(b'[MSG:Comando anterior sem confirmacao; nao repetido.]\n')
                self._responses.put(b'error:9\n')
            self._responses.put(b'[MSG:Sessao autenticada renovada na mesma porta.]\n')
        except Exception as exc:
            self.failure = RuntimeError('Falha ao renovar autenticação: ' + str(exc))
            raise
        finally:
            self._recovering = False
            self._ready.set()

    @property
    def port(self):
        # Preserve the pyserial interface consumed by App.update_indicators().
        return getattr(self.raw, 'port', getattr(self.raw, 'name', 'USB'))

    @property
    def name(self):
        return self.port

    @property
    def is_open(self):
        return not self._closed and self.raw.is_open

    def _pump(self):
        try:
            while self.is_open:
                self._maybe_receipt_probe()
                response = self._read_line()
                if not response:
                    continue
                self._track_status(response)
                text = response.strip().lower()
                if text == b'[ffrt:ok]':
                    continue
                if text == b'[ffrt:err]':
                    self.failure = RuntimeError('Retomada/override não autenticado. Pare e reconecte.')
                    self._responses.put(b'error:110\n')
                    self._ready.set()
                    continue
                if text.startswith(b'grbl') or text == b'[ffsession:reset]':
                    self._responses.put(response)
                    self._recover_session()
                    continue
                if self._consume_receipt(response):
                    continue
                if text == b'ok' or text.startswith(b'error:'):
                    kind, self._kind = self._kind, None
                    if text == b'error:78':
                        self._responses.put(response)
                        self._recover_session()
                        continue
                    # Clear metadata before waking the next sender.
                    self._pending_command = self._pending_since = None
                    self._pending_sequence = self._pending_tag = None
                    # G-code, alarm and limit errors reject that operation, not authentication.
                    self._ready.set()
                    if kind == 'rt':
                        # Realtime API has no GRBL line in the application's inflight queue.
                        continue
                self._responses.put(response)
        except Exception as exc:
            self.failure = RuntimeError('Conexão/autenticação interrompida: ' + str(exc))
            self._ready.set()
        finally:
            self._responses.put(None)

    def readline(self):
        try:
            value = self._responses.get(timeout=.1)
            if value is None:
                if self.is_open:
                    raise OSError('Leitura da conexão interrompida.')
                return b''
            return value
        except queue.Empty:
            return b''

    def _signed(self, command, kind, ack_timeout=None):
        limit = self._ack_timeout if ack_timeout is None else float(ack_timeout)
        if ack_timeout is None and re.search(r'G0*4(?![\d.])', command, re.I):
            dwell = re.search(r'P([0-9]+(?:\.[0-9]*)?|\.[0-9]+)', command, re.I)
            if dwell and math.isfinite(float(dwell[1])):
                limit = max(limit, float(dwell[1]) + 30)
        native_pause = re.fullmatch(r'(?:N\d+\s*)?M0+(?:\.0+)?', command.strip(), re.I) is not None
        if math.isnan(limit) or limit <= 0 or (math.isinf(limit) and not native_pause):
            raise ValueError('Prazo de confirmação inválido para este comando.')
        generation = self._generation
        if self._recovering:
            raise RuntimeError('Autenticação sendo renovada; comando não enviado.')
        encoded = command.encode('ascii')
        if not 1 <= len(encoded) <= 200 or any(c < 32 or c > 126 for c in encoded):
            raise ValueError('Cada comando deve ter 1–200 caracteres ASCII, em uma única linha.')
        payload = encoded.hex()
        with self._tx:
            deadline = time.monotonic() + limit
            while not self._ready.wait(.1):
                if not self.is_open:
                    raise OSError('Conexão fechada.')
                if time.monotonic() >= deadline:
                    if self._pending_command and not self._ack_expired():
                        deadline = time.monotonic() + 1
                        continue
                    # Never retry an uncertain motion automatically.
                    self.failure = TimeoutError('Sem confirmação da placa. ' + self.communication_diagnostics() + '. Pare e reconecte; comando não será repetido.')
                    raise self.failure
            if self.failure:
                raise self.failure
            if not self.is_open or self.seq >= 0xffffffff:
                raise RuntimeError('Reconecte para uma nova sessão.')
            seq = str(self.seq)
            tag = mac(self.key, self.nonce + '|' + seq + '|' + payload)
            wire = ('$FFCMD=' + seq + ',' + tag + ',' + payload + '\n').encode('ascii')
            self._kind = kind
            self._ready.clear()
            try:
                with self._wire:
                    if generation != self._generation or self._recovering:
                        self._kind = None
                        raise SessionChanged('Sessão renovada; comando não enviado. Confirme o estado antes de tentar novamente.')
                    self._pending_command = command
                    self._pending_timeout = limit
                    self._pending_sequence = seq
                    self._pending_tag = tag
                    self._pending_since = time.monotonic()
                    if self._write_raw(wire) != len(wire):
                        raise OSError('Escrita incompleta; não repetir movimento.')
                    self.seq += 1
            except SessionChanged:
                self._ready.set()
                raise
            except Exception as exc:
                self.failure = OSError('Falha de envio: ' + str(exc) + '. Reconecte; comando não será repetido.')
                self._ready.set()
                raise

    def write_with_timeout(self, data, ack_timeout):
        return self.write(data, ack_timeout=ack_timeout)

    def write(self, data, ack_timeout=None):
        data = bytes(data)
        if not self.is_open:
            raise OSError('Conexão fechada.')
        if data and all(c in SAFE_REALTIME for c in data):
            # Stop/status/reset bypass HMAC and the pending-command queue.
            if self._recovering and all(c in (ord('?'), 0x80, 0x87) for c in data):
                return len(data)
            # Canonical extended status/hold bypass the legacy $39 setting.
            result = self._write_raw(data.translate(REALTIME_WIRE))
            if result != len(data):
                raise OSError('Escrita realtime incompleta; confira o estado da máquina.')
            # Firmware reports session reset; reader renews it without resending moves.
            return result
        if len(data) == 1 and (data[0] >= 0x80 or data == b'~'):
            self._signed_realtime(data[0])
            return 1
        if not data.endswith(b'\n'):
            raise ValueError('Envie comandos terminados por newline.')
        for line in data.decode('ascii').splitlines():
            if line.strip():
                self._signed(line, 'line', ack_timeout=ack_timeout)
        return len(data)

    def _signed_realtime(self, command):
        if command == ord('~'):
            command = 0x81  # Canonical cycle start remains signed, independent of $39.
        # A resume must not wait for the ACK of a held G38.x command.
        with self._rt_tx:
            generation = self._generation
            if self._recovering:
                raise RuntimeError('Autenticação sendo renovada; aguarde antes de retomar.')
            if self.failure:
                raise self.failure
            if self.rtseq >= 0xffffffff:
                raise RuntimeError('Reconecte para uma nova sessão.')
            seq, value = str(self.rtseq), bytes([command]).hex()
            tag = mac(self.key, self.nonce + '|rt|' + seq + '|' + value)
            wire = b'\xf8' + (seq + ',' + tag + ',' + value + '\n').encode('ascii')
            with self._wire:
                if generation != self._generation or self._recovering:
                    raise RuntimeError('Sessão renovada; retomada não enviada.')
                if self._write_raw(wire) != len(wire):
                    self.failure = OSError('Falha de envio realtime; não repetir automaticamente.')
                    raise self.failure
                self.rtseq += 1

    def close(self):
        self._closed = True
        try:
            with self._wire:
                if self.raw.is_open:self._write_raw(b'$FFBYE\n')
        except Exception:
            pass
        self._ready.set()
        self.raw.close()


def open_authenticated(name, baud=115200, path=None):
    import serial
    key = load_key(path)
    # Existing GUI is USB-first. socket:// is supported for a future TCP client,
    # but TCP/Wi-Fi must be validated on hardware before relying on it.
    raw = serial.serial_for_url(name, baudrate=baud, timeout=.1, write_timeout=2)
    return SignedPort(raw, key)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Conexão autenticada USB CNC_FFST')
    parser.add_argument('port')
    parser.add_argument('--baud', type=int, default=115200)
    args = parser.parse_args()
    port = open_authenticated(args.port,args.baud)
    print('Conexão autenticada; nenhum movimento enviado.')
    port.close()
