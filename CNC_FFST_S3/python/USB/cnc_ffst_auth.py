"""CNC_FFST HMAC v1, shared key carried inside the bundled BIN. No unsigned-motion fallback."""
import argparse
import hashlib
import hmac
import json
import os
from pathlib import Path
import queue
import re
import secrets
import threading
import time

SAFE_REALTIME = {0x18, ord('?'), ord('!'), 0x84, 0x85}


KEY_PREFIX = b'FFST_SHAREDKEY1:'
KEY_SUFFIX = b':FFST_KEY_END'


def load_key(path=None):
    # The matching firmware BIN is bundled as EXE data, so there is no external key file.
    path = Path(path or Path(__file__).with_name('CNC_FFST_S3_0.1.2_USB_FULL_16MB.bin'))
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


def verify_firmware(port, identity_path=None):
    path = Path(identity_path or Path(__file__).with_name('firmware_identity.json'))
    try:
        identity = json.loads(path.read_text(encoding='utf-8'))
        expected = identity['app_image_sha256']
        version = identity['firmware']
    except (OSError, ValueError, KeyError) as exc:
        raise RuntimeError('Manifesto do firmware ausente/inválido. Use o pacote Python completo.') from exc
    lines = exchange(port, '$FFINFO')
    if '[FFFW:' + version + ':' + expected + ']' not in lines:
        raise RuntimeError('A placa não está com o BIN CNC_FFST esperado por este programa.')
    return expected


def mac(key, message):
    return hmac.new(key, message.encode('ascii'), hashlib.sha256).hexdigest()


def exchange(port, command, timeout=8):
    port.write(command.encode('ascii') + b'\n')
    lines = []
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        line = port.readline().decode('ascii', 'replace').strip()
        if not line:
            continue
        lines.append(line)
        if line.startswith('error:'):
            if '[FFUNPAIRED]' in lines:
                raise RuntimeError('Firmware não corresponde à edição de chave fixa.')
            stage = command.split('=', 1)[0]
            raise RuntimeError(f'A placa recusou a autenticação: etapa {stage}, resposta {line}. '
                               'Confira se o BIN CNC_FFST-S3-0.1.2 correspondente está gravado.')
        if line == 'ok':
            return lines
    stage = command.split('=', 1)[0]
    raise TimeoutError(f'A placa não respondeu na etapa {stage}. '
                       'Confira o BIN CNC_FFST-S3-0.1.2, a porta e 115200 baud.')


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
        self.nonce = None
        self.failure = None
        self._closed = False
        self._responses = queue.Queue()
        self._ready = threading.Event()
        self._ready.set()
        self._tx = threading.Lock()
        self._kind = None
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

    def _authenticate(self):
        image_hash = verify_firmware(self.raw, self._identity_path)
        lines = exchange(self.raw, '$FFHELLO')
        matches = [re.fullmatch(r'\[FFNONCE:([0-9a-f]{64}):([0-9a-f]{64})\]', s)
                   for s in lines]
        match = next((m for m in matches if m), None)
        if not match:
            raise RuntimeError('Resposta de autenticação inválida.')
        self.nonce = match[1]
        if not hmac.compare_digest(mac(self.key, 'server|' + self.nonce + '|' + image_hash), match[2]):
            raise RuntimeError('A placa não corresponde à chave local.')
        reply = exchange(self.raw, '$FFAUTH=' + mac(self.key, 'client|' + self.nonce + '|' + image_hash))
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
                response = self.raw.readline()
                if not response:
                    continue
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
                if text == b'ok' or text.startswith(b'error:'):
                    kind, self._kind = self._kind, None
                    if text == b'error:78':
                        self._responses.put(response)
                        self._recover_session()
                        continue
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

    def _signed(self, command, kind):
        generation = self._generation
        if self._recovering:
            raise RuntimeError('Autenticação sendo renovada; comando não enviado.')
        encoded = command.encode('ascii')
        if not 1 <= len(encoded) <= 200 or any(c < 32 or c > 126 for c in encoded):
            raise ValueError('Cada comando deve ter 1–200 caracteres ASCII, em uma única linha.')
        payload = encoded.hex()
        with self._tx:
            deadline = time.monotonic() + 120
            while not self._ready.wait(.1):
                if not self.is_open:
                    raise OSError('Conexão fechada.')
                if time.monotonic() >= deadline:
                    # Never retry an uncertain motion automatically.
                    self.failure = TimeoutError('Sem confirmação da placa. Pare e reconecte; comando não será repetido.')
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
                    if self.raw.write(wire) != len(wire):
                        raise OSError('Escrita incompleta; não repetir movimento.')
                    self.seq += 1
            except SessionChanged:
                self._ready.set()
                raise
            except Exception:
                self.failure = OSError('Falha de envio. Reconecte; comando não será repetido.')
                self._ready.set()
                raise

    def write(self, data):
        data = bytes(data)
        if not self.is_open:
            raise OSError('Conexão fechada.')
        if data and all(c in SAFE_REALTIME for c in data):
            # Stop/status/reset bypass HMAC and the pending-command queue.
            if self._recovering and all(c == ord('?') for c in data):
                return len(data)
            result = self.raw.write(data)
            # Firmware reports session reset; reader renews it without resending moves.
            return result
        if len(data) == 1 and (data[0] >= 0x80 or data == b'~'):
            self._signed_realtime(data[0])
            return 1
        if not data.endswith(b'\n'):
            raise ValueError('Envie comandos terminados por newline.')
        for line in data.decode('ascii').splitlines():
            if line.strip():
                self._signed(line, 'line')
        return len(data)

    def _signed_realtime(self, command):
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
                if self.raw.write(wire) != len(wire):
                    self.failure = OSError('Falha de envio realtime; não repetir automaticamente.')
                    raise self.failure
                self.rtseq += 1

    def close(self):
        self._closed = True
        try:
            with self._wire:
                if self.raw.is_open:self.raw.write(b'$FFBYE\n')
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
