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

## Montador de Páginas — cliente 1.2

Adicione CNC_FFST_Unico.py ao Montador e selecione a entrada App.
Não inclua o Python antigo de fabricação como outra página que dispute a mesma
porta COM. Outros programas/páginas não devem abrir simultaneamente a mesma USB.
Não é necessário adicionar módulo de autenticação, JSON ou BIN como recurso.
Reconstrua o programa montado/EXE para incorporar esta versão; o montador embute
uma cópia do código e não atualiza um aplicativo já gerado automaticamente.

Clique Atualizar, selecione a porta COM real e use 115200 baud. Conectar mostra
agora o andamento e os erros. O BIN 0.3.0 correspondente precisa estar na placa;
se ela ainda estiver na 0.2.0/MKS, a autenticação será recusada. Se continuar sem
conectar, envie a mensagem de erro ou as linhas CONECTAR do log
CNC_PCB_diagnostico_GRBL.log na pasta do programa montado. A chave não é registrada.
