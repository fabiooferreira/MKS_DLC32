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
    output = ROOT/'artifacts/CNC_FFST_S3_Instalador_0.2.0.zip'
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        archive.write(ROOT/'installer/Instalador_CNC_FFST_S3.py', 'Instalador_CNC_FFST_S3.py')
        archive.write(ROOT/'artifacts/UART/CNC_FFST_S3_0.1.0_UART_FULL_16MB.bin',
                      'CNC_FFST_S3_0.1.0_UART_FULL_16MB.bin')
        archive.write(ROOT/'python/UART/CNC_FFST_Unico.py', 'CNC_FFST_Unico.py')
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
    print('Installer package:', output.name, output.stat().st_size, 'bytes; private keys/protected binaries excluded.')


if __name__ == '__main__': main()
