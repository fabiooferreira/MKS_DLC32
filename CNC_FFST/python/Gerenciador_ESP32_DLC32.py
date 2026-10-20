"""CNC_FFST Manager 2.0 — DLC32 V2.1, ESP32 clássico, sem display.
Um arquivo de interface; fontes do firmware e ferramentas são selecionadas à parte.
Não grava eFuses. Python 3.10+ com Tkinter. Consulte GERENCIADOR_ESP32.md.
"""
import datetime
import hashlib
import json
import os
from pathlib import Path
import queue
import re
import shutil
import struct
import subprocess
import sys
import threading
import uuid
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

VERSION = '2.0'
FIELDS = ('FLASH_CRYPT_CNT', 'FLASH_CRYPT_CONFIG', 'DISABLE_DL_ENCRYPT',
          'DISABLE_DL_DECRYPT', 'DISABLE_DL_CACHE', 'JTAG_DISABLE', 'ABS_DONE_0', 'ABS_DONE_1')
VERSIONS = {'esptool': '4.8.1', 'bitstring': '4.3.1', 'pyserial': '3.5', 'platformio': '6.1.18'}
FLASH_BYTES = 4 * 1024 * 1024
ENVIRONMENT = 'cnc_ffst_v2_1'
KEY_PREFIX, KEY_SUFFIX = b'FFST_SHAREDKEY1:', b':FFST_KEY_END'
PROTECTION_REASON = ('Bloqueada: falta um bootloader compatível com criptografia e um procedimento '
                     'de provisionamento/atualização validado em placa real. O BIN atual é normal, '
                     'mesmo quando possui autenticação. Este programa não grava eFuses.')


def stamp():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S_%fZ')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name + '.' + uuid.uuid4().hex + '.part')
    try:
        with temporary.open('x', encoding='utf-8') as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write('\n')
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def read_json(path):
    path = Path(path)
    if path.stat().st_size > 256 * 1024:
        raise ValueError('Arquivo JSON maior que o limite de 256 KB.')
    return json.loads(path.read_text(encoding='utf-8'))


def parse_chip(output):
    mac = re.search(r'MAC:\s*([0-9a-fA-F:]{17})', output)
    chip = re.search(r'Chip is\s+([^\r\n]+)', output)
    crystal = re.search(r'Crystal is\s+([^\r\n]+)', output)
    if not mac or not chip:
        raise ValueError('Identificação do chip incompleta.')
    name = chip.group(1)
    if not name.startswith('ESP32') or re.search(r'ESP32-[SCHP]\d', name):
        raise ValueError('Alvo incompatível: somente ESP32 clássico, não DLC32 MAX/S3.')
    return {'mac': mac.group(1).lower(), 'chip_e_revisao': name,
            'cristal': crystal.group(1) if crystal else 'não identificado'}


def parse_efuses(output):
    start = output.find('{')
    if start < 0:
        raise ValueError('Resposta de eFuses sem JSON.')
    data, _ = json.JSONDecoder().raw_decode(output[start:])
    result = {}
    for name in FIELDS:
        entry = data.get(name, {})
        value = entry.get('value')
        expected = int if name.startswith('FLASH_CRYPT') else bool
        if entry.get('readable') is not True or type(value) is not expected:
            raise ValueError('eFuse ausente, não legível ou inválido: ' + name)
        if name == 'FLASH_CRYPT_CNT' and not 0 <= value <= 127:
            raise ValueError('FLASH_CRYPT_CNT fora da faixa.')
        if name == 'FLASH_CRYPT_CONFIG' and not 0 <= value <= 15:
            raise ValueError('FLASH_CRYPT_CONFIG fora da faixa.')
        if type(entry.get('writeable')) is not bool:
            raise ValueError('Permissão de eFuse desconhecida: ' + name)
        result[name] = {'value': value, 'readable': True, 'writeable': entry['writeable']}
    return result


def encryption_state(efuses):
    value = efuses['FLASH_CRYPT_CNT']['value']
    if type(value) is not int or not 0 <= value <= 127:
        raise ValueError('FLASH_CRYPT_CNT inválido.')
    return 'ativa' if bin(value).count('1') % 2 else 'inativa'


def validate_report(report):
    if report.get('formato') != 'CNC_FFST_DIAGNOSTICO_1':
        raise ValueError('Formato de relatório não reconhecido.')
    identity = report.get('identificacao', {})
    if not re.fullmatch(r'(?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}', str(identity.get('mac', ''))):
        raise ValueError('MAC ausente ou inválido no relatório.')
    if not isinstance(identity.get('chip_e_revisao'), str):
        raise ValueError('Chip/revisão ausentes.')
    parse_chip('Chip is ' + identity['chip_e_revisao'] + '\nMAC: ' + identity['mac'])
    efuses = parse_efuses(json.dumps(report.get('efuses', {})))
    # Não confiar em conclusões ou campos adicionais importados.
    return {'formato': 'CNC_FFST_DIAGNOSTICO_1', 'data_utc': str(report.get('data_utc', ''))[:80],
            'hardware_informado_pelo_usuario': 'MKS DLC32 V2.1 / ESP32-WROOM-32U (confirmar fisicamente)',
            'identificacao': {'mac': identity['mac'].lower(),
                              'chip_e_revisao': identity['chip_e_revisao'][:160],
                              'cristal': str(identity.get('cristal', 'não identificado'))[:80]},
            'flash': str(report.get('flash', 'desconhecida'))[:40],
            'efuses': efuses, 'criptografia_flash': encryption_state(efuses),
            'ativacao_de_protecoes': PROTECTION_REASON,
            'privacidade': 'Sem chaves, blocos de chave, Wi-Fi ou conteúdo da flash.'}


def analyze(report):
    report = validate_report(report)
    blocked = []
    if report['flash'].upper().replace(' ', '') != '4MB':
        blocked.append('Este perfil exige flash de 4 MB.')
    for name, entry in report['efuses'].items():
        if entry['value'] != 0 or not entry['writeable']:
            blocked.append(name + ': estado alterado; exige análise específica antes de gravar.')
    return {'gravacao_normal_permitida': not blocked, 'bloqueios': blocked,
            'criptografia_flash': report['criptografia_flash'],
            'protecao_contra_copia': 'Não certificada por este diagnóstico.',
            'proteger': PROTECTION_REASON,
            'observacao': 'Relatório importado permite análise; gravação exige nova consulta USB.'}


def command(port, operation, path=None):
    # Não aceita comandos livres, --force, erase_flash ou qualquer burn_*.
    base = ['--chip', 'esp32', '--port', port, '--baud', '115200']
    if operation in ('chip', 'flash'):
        return 'esptool', base + [{'chip': 'chip_id', 'flash': 'flash_id'}[operation]]
    if operation == 'efuses':
        return 'espefuse', base + ['summary', '--format', 'json', *FIELDS]
    if operation == 'backup' and path:
        return 'esptool', base + ['--after', 'no_reset', 'read_flash', '0x0', str(FLASH_BYTES), str(path)]
    if operation == 'write' and path:
        return 'esptool', base + ['--after', 'no_reset', 'write_flash', '--flash_mode', 'keep',
                                '--flash_freq', 'keep', '--flash_size', 'keep', '0x0', str(path)]
    if operation == 'verify' and path:
        return 'esptool', base + ['verify_flash', '--diff', 'no', '0x0', str(path)]
    raise ValueError('Operação não permitida.')


def project_info(folder):
    root = Path(folder).expanduser().resolve()
    if (root / 'CNC_FFST/Firmware/platformio.ini').is_file():
        root = root / 'CNC_FFST'
    ini = root / 'Firmware/ini/mks_dlc32.ini'
    header = root / 'Firmware/Grbl_Esp32/src/Grbl.h'
    if not (root / 'Firmware/platformio.ini').is_file() or not ini.is_file() or not header.is_file():
        raise ValueError('Selecione a pasta CNC_FFST com Firmware/platformio.ini e tools/.')
    config = ini.read_text(encoding='utf-8')
    version = re.search(r'GRBL_VERSION_BUILD\s*=\s*"(CNC_FFST-[^"]+)"', header.read_text(encoding='utf-8'))
    if not version or version[1] not in ('CNC_FFST-0.2.0', 'CNC_FFST-0.3.0'):
        raise ValueError('Este gerenciador aceita as fontes CNC_FFST 0.2.0 ou 0.3.0 conhecidas.')
    section = re.search(r'\[env:cnc_ffst_v2_1\]([^\[]*)', config)
    if not section or 'espressif32@3.2.0' not in config:
        raise ValueError('Perfil/pin da plataforma diferente do perfil DLC32 V2.1 conhecido.')
    auth = bool(re.search(r'^\s*-D\s*CNC_FFST_AUTH\s*$', section[1], re.M))
    if auth != (version[1] == 'CNC_FFST-0.3.0'):
        raise ValueError('Versão e flag de autenticação não correspondem; revise o projeto.')
    return {'root': str(root), 'version': version[1], 'auth': auth,
            'environment': ENVIRONMENT, 'flash_encryption': False}


def image_info(data):
    if len(data) < 24 or data[0] != 0xe9 or not 1 <= data[1] <= 16:
        raise ValueError('Cabeçalho de imagem ESP32 inválido.')
    if struct.unpack_from('<H', data, 12)[0] != 0 or data[23] not in (0, 1):
        raise ValueError('Imagem incompatível com ESP32 clássico.')
    pos, checksum = 24, 0xef
    for _ in range(data[1]):
        if pos + 8 > len(data):
            raise ValueError('Cabeçalho de segmento truncado.')
        length = struct.unpack_from('<I', data, pos + 4)[0]
        pos += 8
        if pos + length > len(data):
            raise ValueError('Segmento truncado.')
        for byte in data[pos:pos + length]:
            checksum ^= byte
        pos += length
    end = ((pos + 16) // 16) * 16
    if end > len(data) or data[end - 1] != checksum:
        raise ValueError('Checksum da imagem inválido.')
    digest = hashlib.sha256(data[:end]).digest()
    if data[23] and data[end:end + 32] != digest:
        raise ValueError('SHA256 interno da imagem inválido.')
    return {'image_sha256': digest.hex(), 'length': end + 32 * data[23]}


def inspect_full(path):
    data = Path(path).read_bytes()
    if len(data) != FLASH_BYTES:
        raise ValueError('O BIN completo precisa ter exatamente 4.194.304 bytes.')
    boot = image_info(data[0x1000:0x8000])
    app = image_info(data[0x10000:0x310000])
    if data[0x1000 + 2] != 3 or data[0x1000 + 3] != 0x2f:
        raise ValueError('Bootloader deve usar DOUT / 80 MHz / flash de 4 MB.')
    # Validar tabela huge_app; não aceitar offsets derivados de JSON externo.
    table = data[0x8000:0x9000]
    entries = []
    for offset in range(0, len(table), 32):
        raw = table[offset:offset + 32]
        magic = struct.unpack_from('<H', raw)[0]
        if magic in (0xffff, 0xebeb):
            break
        if magic != 0x50aa:
            raise ValueError('Tabela de partições inválida.')
        _, kind, subtype, address, size, label, flags = struct.unpack('<HBBII16sI', raw)
        entries.append((kind, subtype, address, size, flags))
    expected = [(1, 2, 0x9000, 0x5000, 0), (1, 0, 0xe000, 0x2000, 0),
                (0, 0x10, 0x10000, 0x300000, 0), (1, 0x82, 0x310000, 0xf0000, 0)]
    if entries != expected:
        raise ValueError('Partições diferentes do perfil huge_app DLC32 V2.1.')
    return {'boot': boot, 'app': app, 'sha256': hashlib.sha256(data).hexdigest()}


def validate_package(manifest_path):
    path = Path(manifest_path).resolve()
    manifest = read_json(path)
    if (manifest.get('format') != 'CNC_FFST_PACKAGE_1' or manifest.get('chip') != 'esp32'
            or manifest.get('flash_bytes') != FLASH_BYTES or manifest.get('offset') != 0
            or manifest.get('flash_encryption') is not False):
        raise ValueError('Pacote não é uma imagem normal DLC32 V2.1 suportada.')
    name = manifest.get('file')
    if not isinstance(name, str) or Path(name).name != name or '/' in name or '\\' in name:
        raise ValueError('Nome de BIN inválido no pacote.')
    binary = (path.parent / name).resolve()
    if binary.parent != path.parent:
        raise ValueError('BIN deve estar na mesma pasta do manifesto.')
    info = inspect_full(binary)
    if info['sha256'] != manifest.get('sha256') or info['app']['image_sha256'] != manifest.get('app_image_sha256'):
        raise ValueError('Pacote alterado: hashes não correspondem.')
    # Hash não é assinatura de confiança. Aceitar somente pacotes de fontes locais conhecidas.
    version = manifest.get('firmware')
    if version not in ('CNC_FFST-0.2.0', 'CNC_FFST-0.3.0'):
        raise ValueError('Versão de pacote não suportada.')
    if type(manifest.get('auth')) is not bool or manifest['auth'] != (version == 'CNC_FFST-0.3.0'):
        raise ValueError('Perfil de autenticação inconsistente.')
    data = binary.read_bytes()
    app = data[0x10000:0x10000 + info['app']['length']]
    if version.encode('ascii') + b'\0' not in app:
        raise ValueError('Identificação interna não corresponde à versão declarada.')
    if manifest['auth']:
        if app.count(KEY_PREFIX) != 1:
            raise ValueError('Registro da credencial de autenticação ausente ou duplicado.')
        start = app.index(KEY_PREFIX) + len(KEY_PREFIX)
        if app[start + 32:start + 32 + len(KEY_SUFFIX)] != KEY_SUFFIX:
            raise ValueError('Registro da credencial de autenticação inválido.')
    elif KEY_PREFIX in app:
        raise ValueError('Pacote sem autenticação contém registro de autenticação inesperado.')
    return manifest, binary


class Backend:
    def __init__(self, python, storage, core=None, log=lambda text: None):
        # Preservar o caminho do venv: resolver seu symlink selecionaria o Python global.
        self.python = os.path.abspath(os.path.expanduser(str(python)))
        self.storage = Path(storage).expanduser().resolve()
        self.storage.mkdir(parents=True, exist_ok=True)
        self.core = Path(core).resolve() if core else self.storage / 'platformio-core'
        self.log = log
        self.env = os.environ.copy()
        self.env.update({'PLATFORMIO_CORE_DIR': str(self.core), 'PYTHONIOENCODING': 'utf-8',
                         'PYTHONUNBUFFERED': '1', 'PLATFORMIO_SETTING_ENABLE_TELEMETRY': 'No'})

    def run(self, args, timeout=120, live=False, cwd=None, logfile=None):
        # shell=False: caminhos com espaços não viram comandos.
        proc = subprocess.Popen([self.python, *map(str, args)], stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace',
                                env=self.env, cwd=cwd,
                                creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
        expired = threading.Event()
        def terminate():
            expired.set()
            proc.kill()
        timer = threading.Timer(timeout, terminate)
        timer.daemon = True
        timer.start()
        output = []
        try:
            for line in proc.stdout:
                output.append(line)
                if logfile:
                    logfile.write(line)
                    logfile.flush()
                if live:
                    self.log(line.rstrip())
            code = proc.wait()
        finally:
            timer.cancel()
            proc.stdout.close()
        if expired.is_set():
            raise RuntimeError('Tempo de espera esgotado. Consulte o registro da operação.')
        if code:
            # Só as operações de consulta pública entram aqui; eFuses são filtrados antes de exibir.
            detail = ''.join(output)[-1800:] if 'espefuse' not in args else ''
            raise RuntimeError(f'Ferramenta falhou (código {code}).\n{detail}')
        return ''.join(output)

    def check_tools(self):
        code = ('import importlib.metadata as m,json\nresult={}\nfor n in ' + repr(list(VERSIONS)) +
                ':\n try: result[n]=m.version(n)\n except m.PackageNotFoundError: result[n]="ausente"\n'
                'print(json.dumps(result))')
        found = json.loads(self.run(['-c', code]))
        if found != VERSIONS:
            raise ValueError('Versões incompatíveis. Use Preparar ferramentas. Encontrado: ' + json.dumps(found))
        return found

    def prepare(self):
        target = self.storage / 'venv-ferramentas'
        python = target / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
        if not python.is_file():
            self.log('Criando ambiente isolado para compilação e USB…')
            self.run(['-m', 'venv', target], timeout=180)
        other = Backend(python, self.storage, self.core, self.log)
        self.log('Instalando ferramentas nas versões fixadas…')
        other.run(['-m', 'pip', 'install', *[f'{k}=={v}' for k, v in VERSIONS.items()]],
                  timeout=900, live=True)
        other.check_tools()
        return str(python)

    def device(self, port):
        self.check_tools()
        def read(operation):
            module, args = command(port, operation)
            self.log('Consultando ' + operation + '…')
            return self.run(['-m', module, *args], timeout=100)
        first = parse_chip(read('chip'))
        flash = re.search(r'Detected flash size:\s*([^\r\n]+)', read('flash'))
        if not flash:
            raise ValueError('Tamanho da flash não identificado.')
        efuses = parse_efuses(read('efuses'))
        if parse_chip(read('chip')) != first:
            raise ValueError('A placa mudou durante a consulta.')
        report = validate_report({'formato': 'CNC_FFST_DIAGNOSTICO_1', 'data_utc': stamp(),
                                  'identificacao': first, 'flash': flash[1], 'efuses': efuses})
        directory = self.storage / 'relatorios' / first['mac'].replace(':', '')
        directory.mkdir(parents=True, exist_ok=True)
        write_json(directory / (stamp() + '.json'), report)
        return report

    def preflight(self, port, expected):
        current = self.device(port)
        expected = validate_report(expected)
        if (current['identificacao'] != expected['identificacao'] or current['flash'] != expected['flash']
                or current['efuses'] != expected['efuses']):
            raise ValueError('Identidade ou estado da placa mudou. Consulte e analise novamente.')
        analysis = analyze(current)
        if not analysis['gravacao_normal_permitida']:
            raise ValueError('\n'.join(analysis['bloqueios']))
        return current

    def build(self, folder):
        self.check_tools()
        project = project_info(folder)
        root = Path(project['root'])
        output = self.storage / 'compilacoes' / stamp()
        output.mkdir(parents=True)
        self.log('Compilação: ' + project['version'] + (' COM autenticação.' if project['auth'] else ' SEM autenticação.'))
        self.log('Esta compilação não inclui proteção contra leitura da flash.')
        with (output / 'compilacao.log').open('w', encoding='utf-8') as log:
            if project['auth']:
                # Nunca criar uma nova credencial silenciosamente: preservar o cliente atual.
                seed = root / '.private/shared_key.bin'
                existing = root / 'artifacts/CNC_FFST_0.3.0_FULL_4MB.bin'
                retained = seed.read_bytes() if seed.exists() else None
                data = existing.read_bytes() if existing.exists() else b''
                index = data.find(KEY_PREFIX)
                recovered = None
                if index >= 0 and data.find(KEY_PREFIX, index + 1) < 0:
                    start = index + len(KEY_PREFIX)
                    if data[start + 32:start + 32 + len(KEY_SUFFIX)] == KEY_SUFFIX:
                        recovered = data[start:start + 32]
                if retained is not None and len(retained) != 32:
                    raise ValueError('Credencial retida inválida; compilação interrompida.')
                if retained is None and recovered is None:
                    raise ValueError('Credencial existente não encontrada. Restaure o BIN ou .private; não será criada outra chave.')
                if retained is not None and recovered is not None and retained != recovered:
                    raise ValueError('Credencial privada e BIN existente divergem. Revise antes de compilar.')
                self.run([root / 'tools/prepare_shared_key.py'], live=True, logfile=log)
            self.run(['-m', 'platformio', 'run', '-d', root / 'Firmware', '-e', ENVIRONMENT, '-j', '2'],
                     timeout=3600, live=True, logfile=log)
            built = root / 'Firmware/.pio/build' / ENVIRONMENT
            app = built / 'firmware.bin'
            image_info(app.read_bytes())
            framework = self.core / 'packages/framework-arduinoespressif32'
            full_name = project['version'].replace('-', '_', 1) + '_FULL_4MB.bin'
            binary = output / full_name
            self.run(['-m', 'esptool', '--chip', 'esp32', 'merge_bin', '--output', binary,
                      '--flash_mode', 'dout', '--flash_freq', '80m', '--flash_size', '4MB',
                      '--fill-flash-size', '4MB',
                      '0x1000', framework / 'tools/sdk/bin/bootloader_dout_80m.bin',
                      '0x8000', built / 'partitions.bin',
                      '0xe000', framework / 'tools/partitions/boot_app0.bin',
                      '0x10000', app], live=True, logfile=log)
            info = inspect_full(binary)
            if project['auth']:
                artifacts = root / 'artifacts'
                artifacts.mkdir(exist_ok=True)
                shutil.copy2(app, artifacts / 'firmware.bin')
                shutil.copy2(binary, artifacts / full_name)
                self.run([root / 'tools/write_firmware_identity.py'], live=True, logfile=log)
                self.run([root / 'tools/bundle_python.py'], live=True, logfile=log)
                shutil.copy2(root / 'python/CNC_FFST_Unico.py', output / 'CNC_FFST_Unico.py')
                shutil.copy2(root / 'python/firmware_identity.json', output / 'firmware_identity.json')
            shutil.copy2(app, output / 'firmware_app_0x10000.bin')
            if (built / 'firmware.elf').is_file():
                shutil.copy2(built / 'firmware.elf', output / 'firmware.elf')
        manifest = {'format': 'CNC_FFST_PACKAGE_1', 'manager': VERSION, 'date_utc': stamp(),
                    'chip': 'esp32', 'flash_bytes': FLASH_BYTES, 'offset': 0,
                    'file': full_name, 'firmware': project['version'], 'auth': project['auth'],
                    'flash_encryption': False, 'sha256': info['sha256'],
                    'app_image_sha256': info['app']['image_sha256'], 'environment': ENVIRONMENT}
        write_json(output / 'pacote.json', manifest)
        validate_package(output / 'pacote.json')
        self.log('Pacote concluído: ' + str(output / 'pacote.json'))
        return str(output / 'pacote.json')

    def backup(self, port, report):
        current = self.preflight(port, report)
        directory = self.storage / 'backups' / current['identificacao']['mac'].replace(':', '') / stamp()
        directory.mkdir(parents=True, mode=0o700)
        part = directory / 'flash.bin.part'
        # Criar com acesso privado em sistemas POSIX antes do utilitário abrir o arquivo.
        fd = os.open(part, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        os.close(fd)
        module, args = command(port, 'backup', part)
        self.log('Lendo backup privado da flash. Não compartilhe esse BIN.')
        self.run(['-m', module, *args], timeout=600, live=True)
        if part.stat().st_size != FLASH_BYTES:
            raise ValueError('Backup incompleto. O arquivo .part não pode ser considerado válido.')
        module, args = command(port, 'chip')
        if parse_chip(self.run(['-m', module, *args])) != current['identificacao']:
            raise ValueError('Identificação mudou durante o backup.')
        binary = directory / 'flash.bin'
        os.replace(part, binary)
        write_json(directory / 'backup.json', {'formato': 'CNC_FFST_BACKUP_1', 'data_utc': stamp(),
                   'mac': current['identificacao']['mac'], 'bytes': FLASH_BYTES,
                   'sha256': sha(binary), 'relatorio': current})
        self.log('Backup concluído: ' + str(binary))
        return str(binary)

    def flash(self, port, report, manifest_path):
        manifest, binary = validate_package(manifest_path)
        # Copiar a imagem verificada antes de iniciar para evitar alteração do pacote na origem.
        directory = self.storage / 'gravacoes' / stamp()
        directory.mkdir(parents=True, mode=0o700)
        staged = directory / 'imagem.bin'
        shutil.copy2(binary, staged)
        if sha(staged) != manifest['sha256']:
            raise ValueError('A imagem mudou durante a preparação da gravação.')
        entry = {'formato': 'CNC_FFST_GRAVACAO_1', 'data_utc': stamp(), 'status': 'iniciando',
                 'mac': report['identificacao']['mac'], 'pacote': manifest}
        write_json(directory / 'gravacao.json', entry)
        try:
            current = self.preflight(port, report)
            backup = self.backup(port, current)
            entry['backup'] = backup
            # Reconsultar proteções após o backup e antes de escrever.
            self.preflight(port, current)
            if sha(staged) != manifest['sha256']:
                raise ValueError('Imagem preparada foi alterada.')
            entry['status'] = 'gravando'
            write_json(directory / 'gravacao.json', entry)
            self.log('Gravando imagem completa em 0x0; configurações antigas serão substituídas.')
            with (directory / 'usb.log').open('w', encoding='utf-8') as log:
                for operation in ('write', 'verify'):
                    module, args = command(port, operation, staged)
                    self.run(['-m', module, *args], timeout=900, live=True, logfile=log)
            entry['status'] = 'gravado_e_verificado'
            entry['protecao_de_leitura'] = False
            entry['teste_funcional'] = 'Pendente: boot, autenticação e testes controlados da máquina.'
            self.log('Gravação e comparação da flash concluídas. Teste funcional ainda pendente.')
        except Exception as exc:
            entry['status'] = 'falha'
            entry['erro'] = str(exc)
            raise
        finally:
            write_json(directory / 'gravacao.json', entry)
        return str(directory / 'gravacao.json')


class App(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        self.pack(fill='both', expand=True)
        self.report = None
        self.busy = False
        self.events = queue.Queue()
        self.buttons = []
        base = Path(os.environ.get('CNC_PCBS_CONFIG_DIR', str(Path.home()))) / 'CNC_FFST_Gerenciador'
        self.storage = tk.StringVar(value=str(base))
        managed = base / 'venv-ferramentas' / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
        default_python = str(managed) if managed.is_file() else (sys.executable if not getattr(sys, 'frozen', False) else (shutil.which('python') or ''))
        self.python = tk.StringVar(value=default_python)
        self.port = tk.StringVar()
        self.source = tk.StringVar()
        self.package = tk.StringVar()
        self.status = tk.StringVar(value='Selecione as ferramentas e consulte a placa ou importe um relatório.')
        self.off = tk.BooleanVar(value=False)
        self.board_ok = tk.BooleanVar(value=False)
        ttk.Label(self, text='CNC_FFST — Gerenciador DLC32 V2.1', font=('Arial', 14, 'bold')).pack(anchor='w')
        ttk.Label(self, text='Diagnóstico → Análise → Compilação → Gravação → Proteção', padding=(0, 5)).pack(anchor='w')
        tabs = ttk.Notebook(self)
        tabs.pack(fill='both', expand=True)
        tools = ttk.Frame(tabs, padding=10)
        board = ttk.Frame(tabs, padding=10)
        build = ttk.Frame(tabs, padding=10)
        flash = ttk.Frame(tabs, padding=10)
        security = ttk.Frame(tabs, padding=10)
        for page, title in [(tools, 'Ferramentas'), (board, 'Placa e relatório'), (build, 'Compilar'),
                            (flash, 'Gravar'), (security, 'Proteção')]:
            tabs.add(page, text=title)
        self.path_row(tools, 'Python para as ferramentas:', self.python, file=True)
        self.path_row(tools, 'Pasta de trabalho e backups:', self.storage)
        self.button(tools, 'Preparar ferramentas (requer internet)', self.prepare)
        self.button(tools, 'Verificar ferramentas', self.check)
        self.label(tools, 'Instalação isolada: PlatformIO 6.1.18, esptool 4.8.1, bitstring 4.3.1 e pyserial 3.5. '
                   'O Python precisa ter venv; no Linux, a interface precisa de python3-tk. '
                   'A primeira compilação também baixa a plataforma ESP32.')
        row = ttk.Frame(board)
        row.pack(fill='x')
        ttk.Label(row, text='Porta USB:').pack(side='left')
        self.ports = ttk.Combobox(row, textvariable=self.port, width=25)
        self.ports.pack(side='left', padx=6)
        self.button(row, 'Atualizar portas', self.refresh, side='left')
        self.scan = self.button(board, 'Consultar placa por USB', self.start)
        self.button(board, 'Importar relatório JSON', self.import_report)
        self.button(board, 'Analisar relatório', self.analyze_report)
        self.save = self.button(board, 'Salvar relatório JSON', self.export)
        self.analysis_text = tk.Text(board, height=9, width=90, wrap='word', state='disabled')
        self.analysis_text.pack(fill='both', expand=True, pady=6)
        self.path_row(build, 'Projeto local (pasta CNC_FFST):', self.source)
        self.button(build, 'Conferir perfil do projeto', self.inspect_project)
        self.button(build, 'Compilar e gerar pacote completo', self.build)
        self.label(build, 'Aceita as fontes 0.3.0 COM autenticação ou 0.2.0 SEM autenticação. '
                   'A versão é detectada no projeto; o programa não remove autenticação. '
                   'Na versão 0.3.0 também gera um CNC_FFST_Unico.py correspondente ao novo BIN. '
                   'Estas fontes geram firmware SEM proteção de leitura. Não é preciso conectar a placa para compilar.')
        self.path_row(flash, 'Pacote de compilação (pacote.json):', self.package, file=True)
        self.button(flash, 'Conferir pacote', self.inspect_package)
        self.button(flash, 'Criar backup privado da placa', self.backup)
        self.button(flash, 'Gravar BIN e verificar', self.flash)
        self.label(flash, 'Use somente pacotes produzidos a partir de fontes confiáveis. '
                   'A imagem completa de 4 MB é gravada em 0x0 e substitui calibrações, Wi-Fi e arquivos da placa. '
                   'Um backup privado é obrigatório e automático antes da gravação. '
                   'Não desconecte ou troque a placa durante as operações.')
        self.label(security, PROTECTION_REASON)
        ttk.Button(security, text='Ativar proteções — indisponível', state='disabled').pack(anchor='w', pady=12)
        self.label(security, 'Autenticação do aplicativo e criptografia da flash têm funções diferentes. '
                   'A chave compartilhada de autenticação permanece; a criptografia exigirá uma chave por placa. '
                   'Relatório ou manifesto JSON não autoriza gravar eFuses. '
                   'Gravação convencional em placas com proteções já alteradas será bloqueada.')
        ttk.Checkbutton(self, text='Trabalho parado; laser/spindle desligados; outros controladores fechados.',
                        variable=self.off).pack(anchor='w', pady=(8, 0))
        ttk.Checkbutton(self, text='Confirmei fisicamente: DLC32 V2.1, ESP32-WROOM-32U, sem display.',
                        variable=self.board_ok).pack(anchor='w')
        ttk.Label(self, textvariable=self.status, wraplength=850).pack(anchor='w', pady=5)
        self.log = tk.Text(self, width=105, height=10, wrap='word', state='disabled')
        self.log.pack(fill='both', expand=True)
        self.write('Gerenciador ' + VERSION + '. Nenhuma proteção é ativada automaticamente.')
        self.timer = self.after(100, self.poll)
        self.bind('<Destroy>', self.cleanup, add='+')

    @staticmethod
    def label(parent, text):
        ttk.Label(parent, text=text, wraplength=800, justify='left').pack(anchor='w', pady=8)

    def button(self, parent, text, action, side='top'):
        button = ttk.Button(parent, text=text, command=lambda: self.guard(action))
        button.pack(anchor='w', pady=3, side=side)
        self.buttons.append(button)
        return button

    def guard(self, action):
        if self.busy:
            return
        try:
            action()
        except Exception as exc:
            self.write('ERRO: ' + str(exc))
            messagebox.showerror('Operação não concluída', str(exc), parent=self)

    def path_row(self, parent, label, variable, file=False):
        ttk.Label(parent, text=label).pack(anchor='w', pady=(6, 0))
        row = ttk.Frame(parent)
        row.pack(fill='x')
        ttk.Entry(row, textvariable=variable).pack(side='left', fill='x', expand=True)
        def choose():
            selected = filedialog.askopenfilename(parent=self) if file else filedialog.askdirectory(parent=self)
            if selected:
                variable.set(selected)
        self.button(row, 'Selecionar', choose, side='left')

    def backend(self):
        if not self.python.get().strip() or not Path(self.python.get()).is_file():
            raise ValueError('Selecione o executável Python para as ferramentas.')
        if not self.storage.get().strip():
            raise ValueError('Selecione a pasta de trabalho.')
        return Backend(self.python.get(), self.storage.get(), log=lambda s: self.events.put(('log', s)))

    def hardware(self):
        if not self.off.get() or not self.board_ok.get():
            raise ValueError('Confirme as duas condições abaixo das abas antes de acessar a placa.')
        port = self.port.get().strip()
        if not port:
            raise ValueError('Selecione a porta USB.')
        return port

    def launch(self, work, done):
        self.busy = True
        self.status.set('Executando… acompanhe o registro. Aguarde antes de fechar ou desconectar.')
        for button in self.buttons:
            button.configure(state='disabled')
        def worker():
            try:
                self.events.put(('done', (done, work())))
            except Exception as exc:
                self.events.put(('error', str(exc)))
        threading.Thread(target=worker, daemon=True).start()

    def poll(self):
        try:
            while True:
                kind, value = self.events.get_nowait()
                if kind == 'log':
                    self.write(value)
                else:
                    self.busy = False
                    for button in self.buttons:
                        button.configure(state='normal')
                    if kind == 'done':
                        callback, result = value
                        self.status.set('Operação concluída.')
                        self.guard(lambda: callback(result))
                    else:
                        self.status.set('Falha: operação não concluída.')
                        self.write('ERRO: ' + value)
                        messagebox.showerror('Operação não concluída', value, parent=self)
        except queue.Empty:
            pass
        self.timer = self.after(100, self.poll)

    def cleanup(self, event):
        if event.widget is self:
            self.after_cancel(self.timer)

    def write(self, text):
        self.log.configure(state='normal')
        self.log.insert('end', str(text) + '\n')
        # Limitar o widget; o log completo da compilação permanece em arquivo.
        if int(self.log.index('end-1c').split('.')[0]) > 1200:
            self.log.delete('1.0', '200.0')
        self.log.see('end')
        self.log.configure(state='disabled')

    def prepare(self):
        backend = self.backend()
        self.launch(backend.prepare, lambda path: (self.python.set(path), self.write('Ferramentas prontas: ' + path)))

    def check(self):
        backend = self.backend()
        self.launch(backend.check_tools, lambda result: self.write(json.dumps(result, ensure_ascii=False)))

    def refresh(self):
        backend = self.backend()
        code = 'from serial.tools import list_ports; import json; print(json.dumps([p.device for p in list_ports.comports()]))'
        def done(ports):
            self.ports['values'] = ports
            if ports and self.port.get() not in ports:
                self.port.set(ports[0])
            self.write('Portas encontradas: ' + ', '.join(ports))
        self.launch(lambda: json.loads(backend.run(['-c', code])), done)

    def show_report(self, report):
        self.report = validate_report(report)
        self.analyze_report()

    def start(self):
        port, backend = self.hardware(), self.backend()
        self.report = None
        self.launch(lambda: backend.device(port), self.show_report)

    def import_report(self):
        path = filedialog.askopenfilename(parent=self, filetypes=[('Relatório JSON', '*.json')])
        if path:
            self.show_report(read_json(path))

    def analyze_report(self):
        if self.report is None:
            raise ValueError('Consulte a placa ou importe um relatório primeiro.')
        result = analyze(self.report)
        text = json.dumps({'placa': self.report['identificacao'], 'flash': self.report['flash'],
                           'analise': result}, ensure_ascii=False, indent=2)
        self.analysis_text.configure(state='normal')
        self.analysis_text.delete('1.0', 'end')
        self.analysis_text.insert('end', text)
        self.analysis_text.configure(state='disabled')
        self.write('Relatório analisado. ' + ('Perfil normal elegível para reconsulta antes da gravação.'
                   if result['gravacao_normal_permitida'] else 'Gravação convencional BLOQUEADA.'))

    def export(self):
        if self.report is None:
            raise ValueError('Gere ou importe um relatório primeiro.')
        path = filedialog.asksaveasfilename(parent=self, initialfile='DLC32_' +
                   self.report['identificacao']['mac'].replace(':', '') + '.json', defaultextension='.json')
        if path:
            write_json(path, self.report)
            self.write('Relatório salvo: ' + path)

    def inspect_project(self):
        self.write(json.dumps(project_info(self.source.get()), ensure_ascii=False, indent=2))

    def build(self):
        source = project_info(self.source.get())['root']
        backend = self.backend()
        self.package.set('')
        def done(path):
            self.package.set(path)
            self.inspect_package()
        self.launch(lambda: backend.build(source), done)

    def inspect_package(self):
        manifest, binary = validate_package(self.package.get())
        self.write(json.dumps(manifest, ensure_ascii=False, indent=2))
        self.write('Imagem completa verificada: ' + str(binary))

    def backup(self):
        if self.report is None:
            raise ValueError('Consulte a placa ou importe o relatório primeiro.')
        port, backend = self.hardware(), self.backend()
        report = validate_report(self.report)
        self.launch(lambda: backend.backup(port, report), lambda result: self.write('Backup privado salvo: ' + result))

    def flash(self):
        if self.report is None:
            raise ValueError('Consulte a placa ou importe o relatório primeiro.')
        port, backend = self.hardware(), self.backend()
        report = validate_report(self.report)
        analysis = analyze(report)
        if not analysis['gravacao_normal_permitida']:
            raise ValueError('\n'.join(analysis['bloqueios']))
        path = str(Path(self.package.get()).resolve())
        manifest, binary = validate_package(path)
        label = 'COM autenticação' if manifest['auth'] else 'SEM autenticação'
        if not messagebox.askyesno('Confirmar gravação', f"Placa: {report['identificacao']['mac']} em {port}\n"
                f"Firmware: {manifest['firmware']} {label}\nArquivo: {binary.name}\n"
                'Imagem completa em 0x0, SEM proteção contra leitura.\n'
                'Será criado backup; configurações antigas serão substituídas.\nContinuar?', parent=self):
            return
        self.launch(lambda: backend.flash(port, report, path), lambda result: self.write('Registro da gravação: ' + result))


def create_page(parent):
    return App(parent)


def main():
    root = tk.Tk()
    root.title('CNC_FFST — Gerenciador DLC32 V2.1')
    root.geometry('980x850')
    app = App(root)
    def close():
        if app.busy:
            messagebox.showinfo('Operação em andamento', 'Aguarde a operação terminar antes de fechar.', parent=root)
        else:
            root.destroy()
    root.protocol('WM_DELETE_WINDOW', close)
    root.mainloop()


if __name__ == '__main__':
    main()
