# CNC_FFST 0.3.0 — cliente USB com chave compartilhada embutida

O usuário escolheu uma chave única, igual em todas as placas e incluída no
BIN e no EXE. Não existe pareamento inicial nem arquivo de chave separado.
A conexão autentica os dois lados a cada clique em Conectar. O programa
confere a versão e o hash do firmware rodando antes de autorizar comandos.

## Usar em Python

Mantenha juntos estes arquivos do pacote:
- Fabricação Laser Fresa.py
- cnc_ffst_auth.py
- firmware_identity.json
- CNC_FFST_0.3.0_FULL_4MB.bin

Instale `python -m pip install -r requirements.txt` e execute
`python "Fabricação Laser Fresa.py"`.

Faça backup/calibração antes de gravar o BIN completo 0.3.0 a partir de 0x0;
esta gravação sobrescreve configurações NVS e SPIFFS. Mantenha laser/spindle
sem alimentação durante a gravação e os testes iniciais. Abra o programa,
selecione a porta USB e clique Conectar. Não há botão de pareamento.

Programas comuns continuam consultando/editando calibrações GRBL permitidas,
mas não executam movimentos ou acionam saídas. O programa autenticado mantém
edição de G-code, configurações, sondagem e envio de arquivo. A autenticação
não remove o ALARM inicial nem calibra a máquina.

Depois de Ctrl-X, reset ou falha de autenticação, desconecte e conecte de novo.
Movimentos não são repetidos automaticamente após timeout/perda de confirmação.
Hold/reset/status não precisam esperar a fila de comandos autenticados.

## Gerar EXE no Windows

Execute `gerar_executavel.bat` com Python instalado e acesso ao PyPI.
O resultado será `dist/CNC_FFST_Controlador.exe`. O módulo de autenticação,
o manifesto e o BIN com a chave são empacotados dentro do EXE; não será
necessário deixar um arquivo de chave separado ao lado do executável.
Preserve os recursos/ícones externos usados pelo programa original, se aplicável.

O EXE Windows não foi gerado nem executado neste ambiente Linux. A sintaxe
Python e o protocolo foram testados em computador; a interface Tk, os drivers
USB e o funcionamento físico precisam ser validados no seu Windows/placa.
Wi-Fi ainda não tem uma interface de conexão integrada/validada no programa.

## Limite da exclusividade

A placa verifica a chave compartilhada, não a assinatura do arquivo EXE.
A chave pode ser extraída do BIN ou do EXE, e então outro programa pode
implementar o protocolo. Como a chave é única, uma extração afeta todas as
placas. Isso foi escolhido pelo usuário; não é proteção contra engenharia
reversa. O BIN público necessariamente contém a chave em formato recuperável.
Não existe Secure Boot, criptografia de flash ou atestação de hardware.
A conferência de hash impede incompatibilidades acidentais, mas um firmware
malicioso pode mentir sobre sua identidade. Não gravar eFuses neste procedimento.
