# Pausa para Conferência de Posicionamento e Ajuste Fino

A versão atual é UART/USB 0.1.3 ou protegido 0.2.3 com o Python correspondente. A revisão de comunicação e as instruções de gravação estão em [REVISAO_0.1.3.md](REVISAO_0.1.3.md). Esta página descreve o alinhamento.

Coloque M0 sozinho em uma linha do arquivo (comentários e número N são aceitos). O Python bloqueia as linhas seguintes, aguarda os movimentos anteriores e Idle, salva modos/XYZ, envia M5 e confirma relatórios em mm (`$13=0`). A pausa é gerenciada pelo programa: o M0 não é enviado para deixar o firmware em Hold, porque jog comum é recusado nesse estado. A serial pode mostrar Idle durante a conferência.

A caixa, sem bloquear a janela principal, informa que movimentos e macros estão ativos para ajuste fino de X/Y/Z e que se deve pressionar **Retornar** para continuar. Fechar o aviso mantém a pausa. Use o passo e avanço dos botões existentes ou suas macros de movimento. O botão de jog força G21/G91 para que o passo informado seja em mm. Macros seguem suas próprias unidades G-code.

As macros de ajuste são validadas antes do envio: aceitam XYZ, G0/G1, G90/G91, G20/G21, G94, F positivo, M5 e `$J=`. Não aceitam ligar ferramenta, mover A, homing, sondagem, arcos ou redefinição de origem. Arquivos/macros também respeitam o limite de 200 caracteres ASCII por comando; o arquivo é recusado antes de começar se uma linha exceder seu buffer. Fora da conferência, movimentos/macros têm comportamento normal e atualizam as coordenadas.

Ao receber ACK de `$J`, o Python ainda aguarda status Idle: o ACK pode chegar antes de o jog terminar. Só então executa G4/G92 e restaura os modos do arquivo sem religar a ferramenta. Os ajustes usam avanço por minuto G94, preservando as unidades e os modos originais na retomada. Retornar é recusado durante um ajuste. Somente Retornar autoriza restaurar o estado M3/M4/M5 e S do arquivo e continuar.

G92 atribui à nova posição física o XYZ de trabalho existente ao entrar na conferência. A interface mantém esse XYZ visível durante o ajuste. Exemplo: pausa em X10, ajuste físico +0,1 mm, tela continua X10; X20 do restante do arquivo fica fisicamente +0,1 mm deslocado. Novos ajustes acumulam-se. A posição de máquina MPos continua sendo contada, e limites/emergência não são deslocados nem desativados.

G92 aparece em `$#` e pode persistir conforme a configuração `$384`. O programa não troca essa preferência automaticamente. M2/M30, reset e homing seguem as regras nativas de G92; confira a referência antes de outro trabalho. G53 usa coordenadas físicas de máquina e não recebe o deslocamento de trabalho. Redefinição G10/G92 ou homing após M0 no arquivo são recusados previamente, pois poderiam desfazer o ajuste.

Essa função é para M0 de arquivo real neste programa. Simulação e M0 dentro de uma macro fora de arquivo mantêm pausa/Retornar, mas não habilitam o ajuste físico especial. Feed hold comum também não habilita ajuste. M5 corta o comando elétrico, mas não comprova parada mecânica do spindle sem sensor de rotação.

Emergência, alarme, Hold inesperado, reset, desconexão e falha de ajuste cancelam a continuação, sem repetir movimento, desbloquear ou retomar automaticamente. Se houve deslocamento antes da falha e antes de G92, confira a posição antes de novo trabalho. Desconectar/reconectar encerra workers e zera execução, pausa, filas/progresso do programa e refaz a autenticação; preserva arquivos, macros e configurações reais da placa. Não é restauração de fábrica nem apagamento da origem física.

Testes automatizados usam modelo de coordenadas, Tk e também o núcleo real do grblHAL em simulador. **O ajuste ainda precisa ser validado na ESP32-S3 física**, incluindo limites/homing, emergência, precisão de posição e ferramentas sem potência antes de uso real.
