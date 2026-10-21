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
    output = ROOT/'artifacts/CNC_FFST_S3_Instalador_0.2.3_Revisao.zip'
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        archive.write(ROOT/'installer/Instalador_CNC_FFST_S3.py', 'Instalador_CNC_FFST_S3.py')
        archive.write(ROOT/'artifacts/UART/CNC_FFST_S3_0.1.3_UART_FULL_16MB.bin',
                      'CNC_FFST_S3_0.1.3_UART_FULL_16MB.bin')
        archive.write(ROOT/'python/UART/Fabricação Fresa Laser.py', 'Fabricação Fresa Laser.py')
        archive.writestr('ABRIR_FABRICACAO_FRESA_LASER.cmd', '@echo off\r\nchcp 65001 >nul\r\npy -3.12 "%~dp0Fabricação Fresa Laser.py"\r\npause\r\n')
        archive.writestr('INSTALAR_DEPENDENCIAS_CONTROLE.cmd', '@echo off\r\npy -3.12 -m pip install pyserial==3.5 pillow==11.3.0\r\npause\r\n')
        archive.write(ROOT/'docs/REVISAO_0.1.3.md', 'LEIA_PRIMEIRO.md')
        archive.write(ROOT/'docs/INSTALADOR_E_PROTECAO.md', 'PROTECAO_E_ATUALIZACOES.md')
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
    controller = ROOT/'artifacts/CNC_FFST_S3_UART_0.1.3_Revisao.zip'
    with zipfile.ZipFile(output) as source, zipfile.ZipFile(controller, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in ['Fabricação Fresa Laser.py', 'ABRIR_FABRICACAO_FRESA_LASER.cmd', 'INSTALAR_DEPENDENCIAS_CONTROLE.cmd',
                     'Instalador_CNC_FFST_S3.py', 'ABRIR_INSTALADOR.cmd', 'CNC_FFST_S3_0.1.3_UART_FULL_16MB.bin']:
            archive.writestr(name, source.read(name))
        archive.write(ROOT/'docs/CONFERENCIA_POSICIONAMENTO_XYZ.md', 'GUIA_AJUSTE_XYZ.md')
        archive.write(ROOT/'docs/REVISAO_0.1.3.md', 'REVISAO_E_INSTALACAO.md')
        archive.writestr('LEIA_PRIMEIRO.txt',
            'CNC_FFST-S3 UART 0.1.3 — BIN e Python correspondentes. Leia REVISAO_E_INSTALACAO.md.\n'
            'Salve $$ e $# da placa ANTES de gravar: o BIN completo de 16 MB substitui as configurações na flash.\n'
            'Grave CNC_FFST_S3_0.1.3_UART_FULL_16MB.bin no modo Reversível; depois feche o instalador e use o Python deste pacote.\n'
            'Esta revisão EXIGE BIN 0.1.3 e Python novos juntos. O BIN 0.1.2 não tem a recuperação ACK1.\n'
            'Não gravar imagem reversível em placa já protegida; protegido exige atualização própria com suas chaves existentes.\n'
            'Não aumenta velocidade, muda pinagem ou desativa proteções. Testar primeiro sem potência nas ferramentas.\n'
            'Pausa para Conferência de Posicionamento e Ajuste Fino: fechar aviso mantém pausa; pressione Retornar para continuar.\n'
            'Ajustes XYZ por movimentos/macros existentes usam G92; confira persistência $384 e a referência em $#.\n'
            'Correções incluem leituras fragmentadas, status realtime, confirmação perdida sem reenviar comando, interface e macros assíncronas.\n'
            'Requer Python 3.12: execute INSTALAR_DEPENDENCIAS_CONTROLE.cmd e depois ABRIR_FABRICACAO_FRESA_LASER.cmd.\n'
            'Use a USB CH343, sua COM (exemplo COM8) e 115200 baud. Perfil USB nativo é separado.\n'
            'Testes simulados passaram; motor, sonda, limites, emergência e PWM físicos ainda precisam ser validados.\n')
    print('Installer package:', output.name, output.stat().st_size, 'bytes; private keys/protected binaries excluded.')
    print('Controller package:', controller.name)



if __name__ == '__main__': main()
