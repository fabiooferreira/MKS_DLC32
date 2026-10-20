# Programa em um único arquivo

Use **CNC_FFST_Unico.py**. Interface, autenticação, chave compartilhada (via
BIN comprimido embutido) e identidade do firmware ficam nesse único .py.
Não exige cnc_ffst_auth.py, firmware_identity.json ou BIN ao lado dele.
Os arquivos modulares nesta pasta foram mantidos apenas para desenvolvimento.

Instale as dependências Python normais:

```text
python -m pip install pyserial pillow
python CNC_FFST_Unico.py
```

Requer Python com Tkinter. Configurações, logs e ícones personalizados do usuário
continuam arquivos opcionais de uso do programa, como antes.

A placa precisa estar com o firmware CNC_FFST 0.3.0 correspondente. Se já está,
não precisa regravar por causa desta consolidação. Clique Conectar para autenticar
pela USB; não há pareamento inicial. Outros programas continuam configurando
parâmetros permitidos, mas a execução exige comandos assinados.

Para gerar EXE Windows, use gerar_executavel.bat ou PyInstaller com esse único
arquivo como entrada, sem --add-data. A chave e os dados do firmware serão incluídos.
A geração do EXE e a GUI Windows ainda precisam ser testadas no computador real.
11 testes do protocolo passaram usando o módulo extraído do arquivo único.

A chave continua sendo recuperável do PY/EXE/BIN; não é proteção contra engenharia
reversa. Não houve alteração do firmware, da pinagem ou das rotinas de usinagem.
