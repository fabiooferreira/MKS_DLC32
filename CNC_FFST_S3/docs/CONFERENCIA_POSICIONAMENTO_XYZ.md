# Pausa para Conferência de Posicionamento e Ajuste Fino

Esta função pertence ao Python CNC_FFST ESP32-S3 autenticado. O BIN reversível UART/USB continua 0.1.2; protegido continua 0.2.2. Nenhuma pinagem, proteção, versão ou byte do firmware foi alterado. Se o BIN correspondente já está instalado, substitua somente o Python. O kit UART é para o modo reversível e a USB CH343. Para protegido, use o Python correspondente gerado localmente, não o programa UART reversível.

## Uso

Insira `M0` sozinho em uma linha do arquivo (comentários e número N são aceitos). O programa aguarda confirmações e término físico do planejamento, consulta Idle, registra modos e posição XYZ, envia M5 e confirma relatórios em mm (`$13=0`). Só depois habilita os ajustes e abre uma caixa sem bloqueio com o título **Pausa para Conferência de Posicionamento e Ajuste Fino**.

A caixa informa que comandos de posição e macros estão ativos e que é necessário pressionar **Retornar** na janela principal para continuar. Fechar o aviso não retoma. Os botões X/Y/Z usam o passo e o avanço escolhidos, em mm. As macros e o campo de comando existentes também servem para os ajustes. Não há novo comando para digitar e não são necessários botões físicos adicionais.

Durante essa pausa, macros são inteiramente validadas antes de enviar qualquer linha. Aceitam movimentos XYZ com G0/G1, G90/G91, G20/G21, G94, avanço F positivo, M5 e jog `$J=`. Não aceitam ligar ferramentas, mover A, sondar, fazer homing, arcos ou redefinir origens. Exemplos de ajuste: `$J=G21 G91 X0.1 F100`, ou macro `G91`, `G1 Z-0.05 F50`, `G90` em linhas separadas. Macros seguem suas unidades G-code; os botões de jog especificam G21 explicitamente. Durante o ajuste usa-se avanço por minuto G94, restaurando os modos originais depois.

O botão Retornar recusa a retomada enquanto há ajuste em execução. Depois do ajuste, os modos, avanço e unidades do arquivo são restaurados sem religar a ferramenta. Somente Retornar autoriza restaurar M3/M4/M5 e S originais e continuar as linhas restantes. M5 corta o comando elétrico; sem sensor de rotação não comprova a parada mecânica do spindle.

## Coordenadas e funcionamento técnico

A pausa é **gerenciada pelo Python**, não é um jog que ignora o Hold do firmware. O M0 do arquivo não é transmitido à placa: o remetente bloqueia as linhas seguintes, drena os movimentos com G4 e deixa o grblHAL em Idle com M5. Assim os movimentos manuais usam o caminho normal, autenticado, do firmware, inclusive limites e emergência. Feed hold comum não habilita o ajuste. O estado da serial pode indicar Idle durante a conferência; o indicador de trabalho e a caixa identificam a pausa.

Ao concluir cada macro/jog e confirmar parada, o programa usa G21/G90 e `G92 X... Y... Z...` para atribuir à nova posição física as coordenadas de trabalho que existiam ao entrar na pausa. Durante o ajuste, a interface mantém esse XYZ de trabalho visível. A posição de máquina MPos **continua sendo contada**, e os limites físicos não são deslocados nem desativados. Isso é uma mudança de referência de trabalho, não perda de passos ou pulso oculto.

Exemplo: o programa pausa em X10, o operador avança fisicamente +0,1 mm, e a tela continua X10. Após Retornar, X20 do arquivo fica fisicamente 0,1 mm deslocado. Um novo ajuste acumula-se sobre o anterior. A e os demais modos que a macro não pode alterar ficam preservados.

G92 não é apenas uma transformação gráfica: aparece nos parâmetros `$#` e seu comportamento de persistência/reset segue as configurações do grblHAL. Pode ser gravado na flash conforme a opção de G92 não volátil existente no firmware. Não se elimina automaticamente a correção ao terminar o arquivo, porque isso mudaria as coordenadas de trabalho; M2/M30, reset e homing seguem as regras nativas de restauração de G92. Confira a referência e `$#` antes do próximo trabalho ou após reset/reconexão. Movimentos explícitos em coordenadas de máquina, como G53, continuam usando a referência física, sem o deslocamento G92.

Arquivos com redefinição G10/G92 ou homing após um M0 são recusados antes de começar: esses comandos poderiam desfazer o alinhamento. Separe M0 de outras instruções na mesma linha. A função de ajuste é para M0 de arquivo real neste programa; pausas na simulação ou M0 enviado dentro de uma macro fora de arquivo não habilitam ajuste físico.

## Falhas e validação

Emergência, alarme, Hold inesperado, reset, desconexão ou falha de ajuste cancelam a continuação; o programa não repete movimentos nem desbloqueia/reinicia automaticamente. Se a falha ocorre após deslocamento e antes de G92, as coordenadas podem ter mudado: conferir posição antes de novo trabalho. Limites por software dependem de homing e das configurações existentes. Não se declara proteção de percurso em máquina não referenciada/configurada.

Testes usam o Streamer/leitor reais com modelo de coordenadas GRBL: XYZ, jog, macros, correção acumulada, referência anterior, arquivo em polegadas, retomada explícita, M5, macro insegura, recusa de retomada durante ajuste, reset, alarme e movimento normal fora da pausa. GUI Tk verifica título exato, comandos/macros disponíveis, caixa sem grab, fechamento sem retomada e Retornar explícito. A autenticação e os testes anteriores de streaming/GUI são preservados. Logs em `artifacts/validation/m0-*.log`.

**Ainda não validado em ESP32-S3 físico.** Testar inicialmente sem potência nas ferramentas, confirmar os relatórios de posição de trabalho e máquina antes/depois de um ajuste pequeno, testar Retornar, emergência e cancelamento. Nenhum ensaio de motor, sondagem ou segurança física foi realizado na nuvem.

Resultado automatizado desta entrega: 11 testes de ajuste, 3 de streaming e 23 de autenticação passaram; diálogo Tk e interface standalone nos perfis UART/USB/protegido e dentro do Montador passaram. Não houve compilação nova: os BINs republicados são idênticos aos anteriores e somente o Python mudou.

## Correção dos botões após Destravar

A habilitação das macros agora depende de execução real (`stream.running`) e das condições da conferência, sem usar o arquivo selecionado (`active_file`) como trava. Esse identificador podia permanecer após interrupção, fazendo o clique em Destravar desabilitar outros botões mesmo com o remetente parado. O ciclo da interface atualiza os botões periodicamente para refletir também o término de workers. Durante execução normal ou ajuste em curso, o bloqueio continua. O firmware segue responsável por autenticação, alarmes e limites; habilitar um botão não libera essas proteções. Regressão Tk reproduziu a desativação antiga ao executar `$X` com referência residual de arquivo.

Na desconexão/reconexão, o programa cancela e encerra as threads da sessão anterior, limpa fila de comandos, pausa, ajuste, posições/modal em cache, progresso, temporizador e identificação do trabalho ativo. A nova porta recebe autenticação nova; nenhum arquivo é retomado. Se uma operação antiga não encerrar dentro da espera limitada de 2 s, a nova conexão é recusada até ela encerrar. Arquivos carregados, macros e parâmetros GRBL permanecem; a rotina não envia restauração de fábrica nem elimina G92 físico na placa. Desconectar a interface cancela o envio, mas não substitui Cancelar/emergência para interromper movimento já aceito pelo controlador.

Validação desta correção: o caso `$X` com seleção residual falhou no cliente antigo (`unlock-before.log`, falha esperada de regressão) e passou no corrigido. Testes Tk incluem desconectar/reconectar com pausa/progresso pendentes, sessão autenticada nova e macros habilitadas. Passaram nos três perfis e no Montador. Os 12 testes de ajuste/desconexão, 3 de streaming e o diálogo de conferência também passaram. Validação física permanece pendente.
