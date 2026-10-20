"""Instalador de bancada CNC_FFST ESP32-S3 N16R8. Python 3.12 + esptool 4.8.1.
Não modifica eFuses. BIN completo 16 MB, offset 0x0. Não usar na DLC32 clássica.
"""
from pathlib import Path
import hashlib
import importlib.metadata
import json
import queue
import os
import tempfile
import secrets
import re
import struct
import subprocess
import sys
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk

TITLE = 'Instalador CNC_FFST — ESP32-S3 N16R8'
BIN_NAME = 'CNC_FFST_S3_0.1.0_UART_FULL_16MB.bin'
# BEGIN KNOWN IMAGES
KNOWN_IMAGES = {'510ff661c5885c97c57e9b69b6d4667adb05f8893595bda90faa57384399d3eb': {'protected': False, 'app_offset': 65536, 'partition_offset': 32768, 'app_image_sha256': 'c5c1c2b6e4b3b0b2aff0d8139aa1fe7fcca9678f57148aa25aa237e31df7ac51'}, '31b095ac583a0fb515eef130001e9156443747488679be3f688513b74d2bda61': {'protected': False, 'app_offset': 65536, 'partition_offset': 32768, 'app_image_sha256': 'bbf22da8b2dbb27b69fe85b3086540f75fe483ba4e7e9c93f5c6d0c57258f211'}}
# END KNOWN IMAGES
REGISTRY_PATH = Path(__file__).resolve().with_name('imagens_locais.json')

def load_local_registry():
    if REGISTRY_PATH.exists():
        values = json.loads(REGISTRY_PATH.read_text(encoding='utf-8'))
        if not isinstance(values, dict): raise ValueError('Registro local inválido.')
        KNOWN_IMAGES.update(values)

SECURITY_FIELDS = ('SPI_BOOT_CRYPT_CNT', 'SECURE_BOOT_EN', 'DIS_DOWNLOAD_MODE',
    'ENABLE_SECURITY_DOWNLOAD', 'DIS_DOWNLOAD_MANUAL_ENCRYPT', 'HARD_DIS_JTAG',
    'SOFT_DIS_JTAG', 'DIS_USB_JTAG', *('KEY_PURPOSE_' + str(i) for i in range(6)))


def validate_image(path):
    data = Path(path).read_bytes()
    if len(data) != 16 * 1024 * 1024:
        raise ValueError('Escolha o BIN COMPLETO de 16 MB; aplicação separada não é aceita.')
    metadata = KNOWN_IMAGES.get(hashlib.sha256(data).hexdigest())
    if metadata is None:
        raise ValueError('BIN não reconhecido por esta versão do instalador. Use um arquivo do pacote correspondente.')
    for offset, label in [(0, 'bootloader'), (metadata['app_offset'], 'aplicação')]:
        image = data[offset:]
        if image[0] != 0xE9 or struct.unpack_from('<H', image, 12)[0] != 9:
            raise ValueError(f'{label}: imagem não corresponde ao ESP32-S3 no endereço esperado.')
        if image[23] != 1 or not 1 <= image[1] <= 16:
            raise ValueError(f'{label}: cabeçalho inválido ou sem SHA256.')
        pos, checksum = 24, 0xEF
        for _ in range(image[1]):
            if pos + 8 > len(image):
                raise ValueError('BIN truncado.')
            length = struct.unpack_from('<I', image, pos + 4)[0]
            pos += 8
            if length > len(image) - pos:
                raise ValueError('Segmento inválido.')
            for byte in image[pos:pos + length]:
                checksum ^= byte
            pos += length
        end = ((pos + 16) // 16) * 16
        if end + 32 > len(image) or image[end - 1] != checksum:
            raise ValueError(f'{label}: checksum inválido.')
        if hashlib.sha256(image[:end]).digest() != image[end:end + 32]:
            raise ValueError(f'{label}: SHA256 inválido.')
    if data[metadata['partition_offset']:metadata['partition_offset'] + 2] != b'\xaa\x50':
        raise ValueError('Tabela de partições ausente no endereço esperado.')
    return hashlib.sha256(data).hexdigest()


def check_dependencies():
    for package, version in [('esptool', '4.8.1'), ('bitstring', '4.3.1'), ('pyserial', '3.5')]:
        try:
            actual = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            actual = 'ausente'
        if actual != version:
            raise RuntimeError(f'{package}: {actual}. Clique em Instalar dependências.')


class Backend:
    def __init__(self, log):
        self.log = log

    def command(self, args):
        command = ([sys.executable, '-u', *args[1:]] if args[0]=='@script'
                   else [sys.executable, '-u', '-m', *args])
        self.log('> python -m ' + ' '.join(args))
        flags = subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0
        with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                              text=True, encoding='utf-8', errors='replace',
                              creationflags=flags) as process:
            lines = []
            for line in process.stdout:
                lines.append(line)
                self.log(line.rstrip())
            code = process.wait()
        if code:
            raise RuntimeError(f'Comando falhou (código {code}). Consulte o registro acima.')
        return ''.join(lines)

    def inspect(self, port):
        if not port.strip():
            raise ValueError('Selecione a porta USB/serial.')
        base = ['esptool', '--chip', 'esp32s3', '--port', port]
        chip = self.command(base + ['chip_id'])
        if not re.search(r'Chip is\s+ESP32-S3\b', chip):
            raise ValueError('A placa não foi identificada como ESP32-S3.')
        flash = self.command(base + ['flash_id'])
        if not re.search(r'Detected flash size:\s*16MB\b', flash):
            raise ValueError('A flash não foi identificada como 16 MB. Gravação bloqueada.')
        match = re.search(r'MAC:\s*([0-9a-fA-F:]{17})', chip)
        if not match: raise ValueError('MAC não identificado.')
        self.log('Placa identificada: ESP32-S3, flash 16 MB. PSRAM e pinagem não são verificadas por esta consulta.')
        return match[1].replace(':', '').lower()

    def security_preflight(self, port):
        output = self.command(['espefuse', '--chip', 'esp32s3', '--port', port,
            'summary', '--format', 'json', *SECURITY_FIELDS])
        begin = output.find('{')
        if begin < 0:
            raise ValueError('Não foi possível consultar os eFuses.')
        fields, _ = json.JSONDecoder().raw_decode(output[begin:])
        for name in SECURITY_FIELDS:
            entry = fields.get(name)
            if not isinstance(entry, dict) or 'value' not in entry:
                raise ValueError('Relatório incompleto: ' + name)
            value = entry['value']
            if name.startswith('KEY_PURPOSE_'):
                fresh = value in ('USER', 'USER (0)', 0, '0')
            else:
                fresh = value in (False, 0, '0', '0x0', '0x00')
            if not fresh:
                raise ValueError('Placa já provisionada ou incompatível: ' + name +
                    '. Não será tentado contornar as proteções.')
        return fields

    def install(self, port, path, protected=False, vault=None, backup=None):
        digest = validate_image(path)
        metadata = KNOWN_IMAGES[digest]
        if bool(metadata['protected']) != bool(protected):
            raise ValueError('O BIN não corresponde ao modo escolhido. Gravação bloqueada.')
        self.log('BIN validado. SHA256: ' + digest)
        mac = self.inspect(port)
        if protected:
            self.check_owner_key(vault, metadata)
            self.security_preflight(port)
            device = self.prepare_keys(mac, vault, backup, metadata)
            self.command(['espefuse', '--chip', 'esp32s3', '--port', port, '--do-not-confirm',
                'burn_key', 'BLOCK_KEY0', str(device/'key_part1.bin'), 'XTS_AES_256_KEY_1',
                'BLOCK_KEY1', str(device/'key_part2.bin'), 'XTS_AES_256_KEY_2'])
            self.save_state(device, 'keys_burned')
            self.log('ATENÇÃO: este BIN ativa proteção permanentemente no próximo boot.')
            # Keep the chip in ROM until verification; never boot provisioning firmware here.
            base = ['esptool', '--chip', 'esp32s3', '--port', port, '--no-stub', '--after', 'no_reset']
        else:
            base = ['esptool', '--chip', 'esp32s3', '--port', port]
        self.command(base + ['write_flash', '--flash_mode', 'keep', '--flash_freq', 'keep',
                             '--flash_size', 'keep', '0x0', str(path)])
        verify = base + (['--before', 'no_reset'] if protected else [])
        self.command(verify + ['verify_flash', '0x0', str(path)])
        if protected:
            self.save_state(device, 'pending_first_boot')
            self.log('BIN verificado, mas proteção ainda NÃO confirmada. Aperte RESET uma vez, '
                'mantenha alimentação estável e aguarde pelo menos 60 segundos. '
                'Não interrompa o primeiro boot. Depois use Conferir proteção.')
        else:
            self.log('SUCESSO: gravação e verificação concluídas. Aperte RESET na DevKit.')

    def verify_protection(self, port, path, require_image=True):
        digest = validate_image(path)
        if not KNOWN_IMAGES[digest]['protected']:
            raise ValueError('Selecione o BIN protegido correspondente.')
        # Query the running application, without entering ROM download mode.
        import hmac
        import time
        import serial
        data = Path(path).read_bytes()
        prefix = b'FFST_SHAREDKEY1:'
        if data.count(prefix) != 1:
            raise ValueError('Registro de autenticação inválido.')
        start = data.index(prefix) + len(prefix)
        key = data[start:start + 32]
        with serial.Serial(port, 115200, timeout=0.2, write_timeout=3) as connection:
            time.sleep(3)
            connection.reset_input_buffer()
            nonce = secrets.token_hex(16)
            connection.write(('$FFSEC=' + nonce + '\n').encode('ascii'))
            deadline = time.monotonic() + 8
            while time.monotonic() < deadline:
                line = connection.readline().decode('ascii', 'replace').strip()
                match = re.fullmatch(r'\[FFSEC:([0-9a-f]+):([0-9a-f]{64})\]', line)
                if match:
                    payload = bytes.fromhex(match[1]).decode('ascii')
                    expected = hmac.digest(key, ('security|' + payload).encode(), 'sha256').hex()
                    if not hmac.compare_digest(expected, match[2]):
                        raise ValueError('Resposta de proteção sem autenticação válida.')
                    status = json.loads(payload)
                    if not all(status.get(name) == 1 for name in
                        ('encryption_release', 'secure_boot', 'secure_download', 'jtag_disabled', 'keys_read_protected')):
                        raise ValueError('Proteção incompleta: ' + payload)
                    if status.get('nonce') != nonce:
                        raise ValueError('Resposta antiga ou nonce inválido.')
                    if not re.fullmatch('[0-9a-f]{12}', status.get('mac', '')):
                        raise ValueError('MAC inválido no relatório.')
                    if require_image and status.get('appsha') != KNOWN_IMAGES[digest]['app_image_sha256']:
                        raise ValueError('A placa não está com a aplicação esperada.')
                    self.log('Proteção reportada pelo firmware autenticado: ' + payload)
                    self.log('Isto não substitui teste físico de clonagem em placa de avaliação.')
                    return status
            raise ValueError('Sem resposta de proteção. Estado NÃO confirmado. '
                'Não tente repetir provisionamento às cegas. Preserve o registro e as chaves.')


    @staticmethod
    def check_owner_key(vault, metadata):
        from cryptography.hazmat.primitives import serialization
        if not vault: raise ValueError('Selecione a pasta de chaves.')
        path = Path(vault)/'secure_boot_signing_key.pem'
        if not path.is_file():
            raise ValueError('Falta sua chave de assinatura. Use Preparar firmware protegido no seu computador.')
        private = serialization.load_pem_private_key(path.read_bytes(), password=None)
        public = private.public_key().public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
        if hashlib.sha256(public).hexdigest() != metadata['signing_public_sha256']:
            raise ValueError('Este BIN não foi assinado pela chave da sua pasta. Compile com sua chave.')

    def prepare_project(self, project, vault, backup):
        import shutil
        project, vault, backup = Path(project).resolve(), Path(vault).resolve(), Path(backup).resolve()
        if vault == backup or vault in backup.parents or backup in vault.parents:
            raise ValueError('Chaves e backup devem ficar em pastas separadas.')
        script = project/'tools/build_firmware.py'
        if not script.is_file(): raise ValueError('Escolha a pasta CNC_FFST_S3 do pacote de fontes.')
        if project == vault or project in vault.parents or project == backup or project in backup.parents:
            raise ValueError('Guarde as chaves e o backup fora da pasta de fontes.')
        vault.mkdir(parents=True, mode=0o700, exist_ok=True); backup.mkdir(parents=True, mode=0o700, exist_ok=True)
        owner_key, backup_key = vault/'secure_boot_signing_key.pem', backup/'secure_boot_signing_key.pem'
        if not owner_key.exists():
            if backup_key.exists():
                raise ValueError('Há chave no backup. Restaure-a na pasta principal; não será criada outra.')
            self.command(['espsecure', 'generate_signing_key', '--version', '2', str(owner_key)])
            owner_key.chmod(0o600)
        if backup_key.exists() and backup_key.read_bytes() != owner_key.read_bytes():
            raise ValueError('A chave de assinatura do backup é diferente. Operação bloqueada.')
        if not backup_key.exists():
            shutil.copy2(owner_key, backup_key); backup_key.chmod(0o600)
        # The build signs with the owner's local key; no manufacturer secret is downloaded.
        self.command(['pip', 'install', 'platformio==6.1.18'])
        self.command(['@script', str(script), 'protected', '--signing-key', str(owner_key)])
        artifacts = project/'artifacts/PROTECTED'
        manifest = json.loads((artifacts/'manifest.json').read_text())
        binary = artifacts/manifest['file']
        self.check_owner_key(vault, manifest)
        metadata = {'protected': True, 'app_offset': manifest['application_offset'],
            'partition_offset': manifest['partition_offset'], 'update_size': manifest['update_size'],
            'app_image_sha256': manifest['app_image_sha256'],
            'signing_public_sha256': manifest['signing_public_sha256']}
        KNOWN_IMAGES[manifest['sha256']] = metadata
        validate_image(binary)
        registry = json.loads(REGISTRY_PATH.read_text()) if REGISTRY_PATH.exists() else {}
        registry[manifest['sha256']] = metadata
        REGISTRY_PATH.write_text(json.dumps(registry, indent=2), encoding='utf-8')
        self.log('BIN protegido preparado com sua chave: ' + str(binary))
        return str(binary)

    @staticmethod
    def save_state(device, phase):
        state_file = device/'device.json'
        state = json.loads(state_file.read_text())
        state['phase'] = phase
        temporary = device/'device.json.tmp'
        with os.fdopen(os.open(temporary, os.O_CREAT | os.O_TRUNC | os.O_WRONLY, 0o600), 'w', encoding='utf-8') as out:
            json.dump(state, out, indent=2); out.flush(); os.fsync(out.fileno())
        os.replace(temporary, state_file)

    def prepare_keys(self, mac, vault, backup, metadata):
        if not vault or not backup:
            raise ValueError('Selecione a pasta de chaves e outra pasta de backup.')
        vault, backup = Path(vault).resolve(), Path(backup).resolve()
        if vault == backup or vault in backup.parents or backup in vault.parents:
            raise ValueError('Chaves e backup precisam de pastas separadas, sem sobreposição.')
        device, copy = vault/mac, backup/mac
        if device.exists() or copy.exists():
            raise ValueError('Já existe registro para este MAC. Não será gerada outra chave nem repetido provisionamento.')
        device.mkdir(parents=True, mode=0o700); copy.mkdir(parents=True, mode=0o700)
        key = secrets.token_bytes(64)
        import shutil
        signing = vault/'secure_boot_signing_key.pem'
        backup_signing = backup/'secure_boot_signing_key.pem'
        if backup_signing.exists() and backup_signing.read_bytes() != signing.read_bytes():
            raise ValueError('Backup da chave de assinatura não confere.')
        if not backup_signing.exists():
            shutil.copy2(signing, backup_signing); backup_signing.chmod(0o600)
        for folder in (device, copy):
            for name, data in [('flash_key.bin', key), ('key_part1.bin', key[:32]), ('key_part2.bin', key[32:])]:
                with os.fdopen(os.open(folder/name, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600), 'wb') as out:
                    out.write(data); out.flush(); os.fsync(out.fileno())
            state = {'mac': mac, 'phase': 'prepared', 'key_sha256': hashlib.sha256(key).hexdigest(),
                     'signing_public_sha256': metadata['signing_public_sha256'],
                     'application_offset': metadata['app_offset'], 'flash_mb': 16}
            state_file = folder/'device.json'
            state_file.write_text(json.dumps(state, indent=2)); state_file.chmod(0o600)
        for folder in (device, copy):
            if (folder/'flash_key.bin').read_bytes()!=key or (folder/'key_part1.bin').read_bytes()!=key[:32] or (folder/'key_part2.bin').read_bytes()!=key[32:]:
                raise ValueError('Chaves/backup não conferem. Nenhum eFuse deve ser gravado.')
        self.log('Chave exclusiva e backup criados para MAC ' + mac + '. Nenhum valor de chave será mostrado.')
        return device

    def update_protected(self, port, path, vault):
        digest = validate_image(path)
        metadata = KNOWN_IMAGES[digest]
        if not metadata['protected']: raise ValueError('Atualização exige BIN protegido autorizado.')
        status = self.verify_protection(port, path, require_image=False)
        if status.get('maintenance_safe') != 1:
            raise ValueError('Pare a máquina e desligue as ferramentas antes de atualizar.')
        device = Path(vault)/status['mac']
        state = json.loads((device/'device.json').read_text())
        key_file = device/'flash_key.bin'
        key = key_file.read_bytes()
        if len(key) != 64 or hashlib.sha256(key).hexdigest() != state['key_sha256']:
            raise ValueError('Chave local inválida ou corrompida.')
        if state['mac'] != status['mac'] or state['signing_public_sha256'] != metadata['signing_public_sha256']:
            raise ValueError('Registro da placa ou chave de assinatura incompatível.')
        if state['application_offset'] != metadata['app_offset']:
            raise ValueError('Atualização não pode mudar o layout das partições.')
        with tempfile.TemporaryDirectory(prefix='ffst-update-') as temporary:
            temporary = Path(temporary)
            plain, cipher = temporary/'application.bin', temporary/'application_encrypted.bin'
            offset = metadata['app_offset']
            plain.write_bytes(Path(path).read_bytes()[offset:offset + metadata['update_size']])
            self.command(['espsecure', 'encrypt_flash_data', '--aes_xts', '--keyfile', str(key_file),
                '--output', str(cipher), '--address', hex(offset), str(plain)])
            self.save_state(device, 'update_pending')
            base = ['esptool', '--chip', 'esp32s3', '--port', port, '--no-stub']
            report = self.command(base + ['--after', 'no_reset', 'get_security_info'])
            if 'Secure Boot: Enabled' not in report or 'Flash Encryption: Enabled' not in report:
                raise ValueError('ROM não confirmou Secure Boot e criptografia. Atualização bloqueada.')
            # --force is confined to known, signed, HOST-ENCRYPTED application bytes.
            # Never use --encrypt: release mode disallows encryption by the ROM.
            self.command(base + ['--before', 'no_reset', '--after', 'hard_reset', 'write_flash',
                '--force', '--flash_mode', 'keep', '--flash_freq', 'keep', '--flash_size', 'keep',
                hex(offset), str(cipher)])
        self.verify_protection(port, path, require_image=True)
        self.save_state(device, 'update_confirmed')
        self.log('Atualização confirmada pela aplicação autenticada, hash e estado das proteções.')


class App:
    def __init__(self, root):
        load_local_registry()
        self.root = root
        self.busy = False
        self.events = queue.Queue()
        self.backend = Backend(lambda text: self.events.put(('log', text)))
        root.title(TITLE)
        root.geometry('1040x760')
        root.minsize(700, 520)
        frame = ttk.Frame(root, padding=14)
        frame.pack(fill='both', expand=True)
        ttk.Label(frame, text=TITLE, font=('', 14, 'bold')).pack(anchor='w')
        ttk.Label(frame, text='Use a USB/serial. Desligue a alimentação dos motores, laser e spindle.\n'
                  'Reversível: gravação normal. Protegido: eFuses permanentes e atualizações autorizadas por USB.',
                  wraplength=820).pack(anchor='w', pady=10)
        row = ttk.Frame(frame); row.pack(fill='x', pady=5)
        ttk.Label(row, text='Porta:').pack(side='left')
        self.port = tk.StringVar()
        self.ports = ttk.Combobox(row, textvariable=self.port, width=22)
        self.ports.pack(side='left', padx=8)
        self.buttons = []
        self.button(row, 'Atualizar portas', self.refresh).pack(side='left')
        self.button(row, 'Conferir placa', self.inspect).pack(side='left', padx=8)
        row = ttk.Frame(frame); row.pack(fill='x', pady=5)
        ttk.Label(row, text='BIN:').pack(side='left')
        nearby = Path(__file__).resolve().with_name(BIN_NAME)
        self.path = tk.StringVar(value=str(nearby) if nearby.exists() else '')
        self.entry = ttk.Entry(row, textvariable=self.path)
        self.entry.pack(side='left', fill='x', expand=True, padx=8)
        self.button(row, 'Selecionar BIN', self.browse).pack(side='left')
        self.accept = tk.BooleanVar()
        self.checkbox = ttk.Checkbutton(frame, variable=self.accept,
            text='Estou usando a DevKit ESP32-S3 N16R8 e as cargas estão sem alimentação.')
        self.checkbox.pack(anchor='w', pady=8)
        self.protected = tk.BooleanVar(value=False)
        modes = ttk.Frame(frame); modes.pack(fill='x', pady=5)
        self.reversible_radio = ttk.Radiobutton(modes, variable=self.protected, value=False, text='Reversível')
        self.reversible_radio.pack(side='left')
        self.protection_box = ttk.Radiobutton(modes, variable=self.protected, value=True,
            text='Protegido com atualizações (proteções permanentes)')
        self.protection_box.pack(side='left', padx=20)
        self.vault = tk.StringVar(); self.backup = tk.StringVar()
        for title, variable in [('Pasta de chaves', self.vault), ('Pasta de backup', self.backup)]:
            row = ttk.Frame(frame); row.pack(fill='x', pady=3)
            self.button(row, title, lambda v=variable: self.choose_folder(v)).pack(side='left')
            ttk.Label(row, textvariable=variable, wraplength=750).pack(side='left', padx=8)
        row = ttk.Frame(frame); row.pack(fill='x')
        self.button(row, 'Instalar dependências', self.dependencies).pack(side='left')
        self.button(row, 'GRAVAR E VERIFICAR', self.install).pack(side='left', padx=12)
        self.button(row, 'Atualizar placa protegida', self.update_protected).pack(side='left', padx=5)
        row = ttk.Frame(frame); row.pack(fill='x', pady=5)
        self.button(row, 'Preparar firmware protegido', self.prepare_project).pack(side='left', padx=5)
        self.button(row, 'Conferir proteção', self.verify_protection).pack(side='left')
        self.button(row, 'Salvar registro', self.save_log).pack(side='right')
        self.status = tk.StringVar(value='Pronto. Selecione a porta e o BIN completo.')
        ttk.Label(frame, textvariable=self.status, wraplength=820).pack(anchor='w', pady=10)
        self.progress = ttk.Progressbar(frame, mode='indeterminate')
        self.progress.pack(fill='x')
        logframe = ttk.Frame(frame); logframe.pack(fill='both', expand=True, pady=8)
        self.log = tk.Text(logframe, wrap='word', state='disabled', font=('Consolas', 10))
        scroll = ttk.Scrollbar(logframe, command=self.log.yview)
        self.log.configure(yscrollcommand=scroll.set)
        scroll.pack(side='right', fill='y'); self.log.pack(fill='both', expand=True)
        root.protocol('WM_DELETE_WINDOW', self.close)
        self.refresh()
        root.after(100, self.poll)

    def button(self, parent, text, command):
        button = ttk.Button(parent, text=text, command=command)
        self.buttons.append(button)
        return button

    def refresh(self):
        try:
            from serial.tools import list_ports
            ports = list(list_ports.comports())
            self.ports['values'] = [p.device for p in ports]
            if ports and self.port.get() not in self.ports['values']:
                self.port.set(ports[0].device)
        except ImportError:
            self.status.set('Instale as dependências para listar as portas.')

    def browse(self):
        path = filedialog.askopenfilename(filetypes=[('Firmware BIN', '*.bin')])
        if path:
            self.path.set(path)

    def start(self, action, success):
        if self.busy:
            return
        self.busy = True
        for widget in self.buttons + [self.ports, self.entry, self.checkbox, self.protection_box, self.reversible_radio]:
            widget.configure(state='disabled')
        self.status.set('Em andamento. Não desconecte a placa nem feche o programa.')
        self.progress.start()
        def worker():
            try:
                action()
                self.events.put(('done', success))
            except Exception as error:
                self.events.put(('error', str(error)))
        threading.Thread(target=worker, daemon=True).start()

    def dependencies(self):
        self.start(lambda: self.backend.command(['pip', 'install', 'esptool==4.8.1',
            'bitstring==4.3.1', 'pyserial==3.5']), 'Dependências instaladas. Clique em Atualizar portas.')

    def inspect(self):
        port = self.port.get().strip()
        def action():
            check_dependencies()
            self.backend.inspect(port)
        self.start(action, 'ESP32-S3 com flash de 16 MB identificada.')

    def install(self):
        if not self.accept.get():
            messagebox.showwarning(TITLE, 'Confirme o modelo e desligue a alimentação das cargas.')
            return
        port, path = self.port.get().strip(), Path(self.path.get()).expanduser().resolve()
        try:
            check_dependencies()
            digest = validate_image(path)
            if bool(KNOWN_IMAGES[digest]['protected']) != self.protected.get():
                raise ValueError('BIN incompatível com o modo escolhido. Selecione o BIN correto.')
            if not port:
                raise ValueError('Selecione a porta.')
        except Exception as error:
            messagebox.showerror(TITLE, str(error)); return
        if not messagebox.askyesno(TITLE, f'Gravar em {port}?\n\n{path.name}\n\n'
                                  'Todos os dados existentes na flash serão substituídos.'):
            return
        protected = self.protected.get()
        if protected:
            answer = simpledialog.askstring(TITLE, 'Este procedimento gravará eFuses PERMANENTES, começando pelas chaves.\n'
                'Atualizações USB exigirão a chave desta placa e firmware autorizado.\n'
                'O primeiro boot concluirá as proteções. Uma falha pode inutilizar o módulo.\n'
                'Teste o hardware com o BIN normal antes.\n\n'
                'Digite PROTEGER para autorizar a gravação deste BIN:')
            if answer != 'PROTEGER':
                return
        vault, backup = self.vault.get(), self.backup.get()
        if protected and (not vault or not backup):
            messagebox.showerror(TITLE, 'Selecione as pastas de chaves e backup.'); return
        self.start(lambda: self.backend.install(port, path, protected, vault, backup),
            'BIN verificado. Leia no registro como concluir e conferir a proteção.' if protected
            else 'Gravação e verificação concluídas. Aperte RESET.')

    def prepare_project(self):
        vault, backup = self.vault.get(), self.backup.get()
        if not vault or not backup:
            messagebox.showerror(TITLE, 'Selecione primeiro as pastas de chaves e backup.'); return
        project = filedialog.askdirectory(title='Selecione CNC_FFST_S3 do pacote de fontes')
        if not project: return
        if not messagebox.askyesno(TITLE, 'Instalar ferramentas e compilar no seu computador?\n'
            'Exige internet, espaço em disco e pode demorar vários minutos.\n'
            'Gera sua chave de assinatura e seu BIN. Não grava a placa nesta etapa.'):
            return
        def action():
            check_dependencies()
            result = self.backend.prepare_project(project, vault, backup)
            self.events.put(('path', result))
        self.start(action, 'Firmware protegido preparado com sua chave. Selecione Protegido para gravar.')

    def choose_folder(self, variable):
        path = filedialog.askdirectory()
        if path: variable.set(path)

    def update_protected(self):
        port, path, vault = self.port.get().strip(), Path(self.path.get()).expanduser().resolve(), self.vault.get()
        if not self.accept.get() or not vault:
            messagebox.showwarning(TITLE, 'Desligue as cargas, confirme o modelo e selecione a pasta de chaves.'); return
        if not messagebox.askyesno(TITLE, 'Atualizar a aplicação da placa protegida?\n'
            'Não desconecte a alimentação durante a atualização. Feche o controlador CNC.'):
            return
        def action():
            check_dependencies()
            self.backend.update_protected(port, path, vault)
        self.start(action, 'Atualização protegida concluída e confirmada pelo firmware.')

    def verify_protection(self):
        port, path = self.port.get().strip(), Path(self.path.get()).expanduser().resolve()
        vault = self.vault.get()
        def action():
            check_dependencies()
            status = self.backend.verify_protection(port, path)
            if vault:
                device = Path(vault)/status['mac']
                if (device/'device.json').is_file():
                    self.backend.save_state(device, 'protection_report_confirmed')
        self.start(action, 'Proteção reportada pelo firmware autenticado. Salve o registro.')

    def poll(self):
        while True:
            try:
                kind, text = self.events.get_nowait()
            except queue.Empty:
                break
            if kind == 'path':
                self.path.set(text); continue
            self.log.configure(state='normal'); self.log.insert('end', text + '\n')
            self.log.see('end'); self.log.configure(state='disabled')
            if kind != 'log':
                self.busy = False; self.progress.stop(); self.status.set(text)
                for widget in self.buttons + [self.ports, self.entry, self.checkbox, self.protection_box, self.reversible_radio]:
                    widget.configure(state='normal')
                if kind == 'error':
                    messagebox.showerror(TITLE, text + '\n\nFeche outros programas da porta. '
                        'Se parar em Connecting, segure BOOT, pressione e solte RESET, '
                        'depois solte BOOT quando iniciar. Não use --force.')
        self.root.after(100, self.poll)

    def save_log(self):
        path = filedialog.asksaveasfilename(defaultextension='.txt', initialfile='gravacao_CNC_FFST.txt')
        if path:
            Path(path).write_text(self.log.get('1.0', 'end'), encoding='utf-8')

    def close(self):
        if self.busy:
            messagebox.showwarning(TITLE, 'Aguarde a operação terminar antes de fechar.'); return
        self.root.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    App(root)
    root.mainloop()
