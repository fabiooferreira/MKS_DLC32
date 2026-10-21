"""Package the GUI + reversible image + source. Never include private keys or protected binaries.
Protected firmware must be built by the owner, with the owner's local signing key.
"""
from pathlib import Path
import zipfile
ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'.git', '.pio', '.private', '.platformio-core', '.venv-build', '__pycache__',
            'PROTECTED', 'build', 'dist'}
EXCLUDED_NAMES = {'ffst_key.generated.h', 'compile_commands.json', 'imagens_locais.json',
                  'config_controlador_pcb.json', 'CNC_PCB_diagnostico_GRBL.log'}


def main():
    output = ROOT/'artifacts/CNC_FFST_S3_Instalador_0.2.2_Conferencia_XYZ.zip'
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        archive.write(ROOT/'installer/Instalador_CNC_FFST_S3.py', 'Instalador_CNC_FFST_S3.py')
        archive.write(ROOT/'artifacts/UART/CNC_FFST_S3_0.1.2_UART_FULL_16MB.bin',
                      'CNC_FFST_S3_0.1.2_UART_FULL_16MB.bin')
        archive.write(ROOT/'python/UART/Fabricação Fresa Laser.py', 'Fabricação Fresa Laser.py')
        archive.writestr('ABRIR_FABRICACAO_FRESA_LASER.cmd', '@echo off\r\nchcp 65001 >nul\r\npy -3.12 "%~dp0Fabricação Fresa Laser.py"\r\npause\r\n')
        archive.writestr('INSTALAR_DEPENDENCIAS_CONTROLE.cmd', '@echo off\r\npy -3.12 -m pip install pyserial==3.5 pillow==11.3.0\r\npause\r\n')
        archive.write(ROOT/'docs/INSTALADOR_E_PROTECAO.md', 'LEIA_PRIMEIRO.md')
        archive.writestr('ABRIR_INSTALADOR.cmd', '@echo off\r\npy -3.12 "%~dp0Instalador_CNC_FFST_S3.py"\r\npause\r\n')
        for path in sorted(ROOT.rglob('*')):
            relative = path.relative_to(ROOT)
            if not path.is_file() or path.is_symlink(): continue
            if any(part in EXCLUDED for part in relative.parts): continue
            if path.name in EXCLUDED_NAMES or path.name.startswith('sdkconfig.cnc_ffst'): continue
            if path.suffix.lower() in {'.pem', '.zip', '.pyc'}: continue
            archive.write(path, str(Path('CNC_FFST_S3')/relative))
    with zipfile.ZipFile(output) as archive:
        assert archive.testzip() is None
        assert all('.private' not in Path(name).parts and not name.lower().endswith('.pem') for name in archive.namelist())
        assert not any('/PROTECTED/' in name for name in archive.namelist())
    controller = ROOT/'artifacts/CNC_FFST_S3_UART_0.1.2_Conferencia_XYZ.zip'
    with zipfile.ZipFile(output) as source, zipfile.ZipFile(controller, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in ['Fabricação Fresa Laser.py', 'ABRIR_FABRICACAO_FRESA_LASER.cmd', 'INSTALAR_DEPENDENCIAS_CONTROLE.cmd',
                     'Instalador_CNC_FFST_S3.py', 'ABRIR_INSTALADOR.cmd', 'CNC_FFST_S3_0.1.2_UART_FULL_16MB.bin']:
            archive.writestr(name, source.read(name))
        archive.writestr('LEIA_PRIMEIRO.txt',
            'Fabricação Fresa Laser — ESP32-S3, BIN UART reversível 0.1.2.\n'
            'Correção Python: leitura de ACK/status não fica presa na trava do envio. Inclui a correção de escritas simultâneas. Sem mudança do firmware 0.1.2. Se ele já está gravado, atualize somente o Python. O Emergency Stop continua ativo se a entrada de emergência estiver acionada.\n'
            'Antes de gravar, salve as configurações com $$: este BIN completo substitui as configurações na flash.\n'
            'Gravar o BIN UART 0.1.2 pelo instalador atualizado, no modo Reversível, e usar o programa deste pacote.\n'
            'Se a placa já estiver protegida, NÃO tentar provisionar novamente: exige atualização específica com as chaves existentes.\n'
            'Requer Python 3.12. Execute INSTALAR_DEPENDENCIAS_CONTROLE.cmd uma vez, depois ABRIR_FABRICACAO_FRESA_LASER.cmd.\n'
            'Feche o instalador/outros programas da porta antes de conectar. Use sua COM (exemplo COM8) e 115200 baud.\n'
            'Não usar com DLC32 clássica ou BIN protegido: o controle deve corresponder ao firmware.\n'
            'Para o protegido, use o programa gerado localmente em python/PROTECTED/Fabricação Fresa Laser.py.\n'
            'Movimento, sonda e segurança física ainda exigem testes na placa.\n')
    print('Installer package:', output.name, output.stat().st_size, 'bytes; private keys/protected binaries excluded.')
    print('Controller package:', controller.name)



if __name__ == '__main__': main()
