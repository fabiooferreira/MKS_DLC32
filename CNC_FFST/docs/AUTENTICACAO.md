# CNC_FFST 0.3.0 — controle de execução por chave

Integração baseada no programa `Fabricação Laser Fresa.py` enviado pelo usuário.
USB é o primeiro fluxo de uso; não foi inventado um cliente Wi-Fi de interface
gráfica que o usuário ainda não tem. A versão 0.2.0 permanece na branch anterior.

## Política

Sem chave, outros senders podem consultar parâmetros, estado, offsets, modos,
identificação, listas e reconhecer o alarme com `$X`. Podem editar calibrações
GRBL comuns pelos nomes numéricos ou aliases dos mesmos settings, somente em
Idle/Alarm e com spindle modal desligado: $0–$6, $10–$13, $20–$27, $30–$32,
$38, $40 e parâmetros por eixo $100–$105, $110–$115, $120–$125, $130–$135.
O parâmetro também precisa existir e passar nas validações originais do GRBL.
Consultas de outros settings não ganham permissão extra para executar ações.

Exigem um comando assinado: todos os blocos G-code (exceto M5/M9 exatos e linhas
vazias), G38.x, $H/$HX/etc., $J, acionamento de ferramentas, parâmetros que podem
reconfigurar saídas, scripts de inicialização e apagamento/restauração de NVS.
Os setters de configurações continuam disponíveis no Python autenticado.
O parser G-code e a gramática das configurações permanecem os originais.
Falha de autenticação retorna `error:110`; o bloqueio de alarme GRBL continua
independente e não é removido por autenticar.

Reset Ctrl-X, `?`, hold `!`, safety door e jog cancel continuam públicos.
Retomada `~`, overrides e toggles de spindle/coolant precisam de assinatura.
O toggle de spindle não é tratado como uma parada pública porque pode religar.
Isso não substitui o botão físico de emergência, nem garante que hold desligue
a ferramenta em todos os modos. M5 e reset continuam sendo caminhos de parada.

Scripts de startup não são executados automaticamente neste perfil e o parking
automático foi desabilitado para evitar movimento provocado por uma porta/hold
sem autenticação. O comando de safety door continua solicitando parada/desligamento
pelo caminho GRBL original, sem retração automática. Ações WebUI/SD assíncronas
(WEBCMD) estão bloqueadas inclusive quando encapsuladas; executar jobs no cartão
não é suportado nesta integração. Não confundir configurar GRBL com liberar toda
ação administrativa ESP3D/WebUI. A pinagem não foi alterada.

## Protocolo v1

- `$FFINFO`: retorna versão e SHA256 embutido da aplicação rodando. O programa
  confere o manifesto público `firmware_identity.json` antes da autenticação.
- Chave fixa de 32 bytes compilada no BIN, igual em todas as placas. O pacote
  Python inclui o BIN correspondente como recurso e extrai internamente a mesma
  chave; PyInstaller inclui esse recurso dentro do EXE. Não há arquivo de chave
  externo nem pareamento inicial. `$FFPAIR` é recusado na USB e na rede.
- `$FFHELLO`: novo nonce aleatório de 32 bytes para o transporte, prova HMAC do
  servidor sobre `server|nonce|hash`. Não transmite a chave.
- `$FFAUTH=<HMAC>`: cliente prova `client|nonce|hash`. Um único sucesso por nonce;
  repetir a prova não permite zerar o contador e repetir movimentos.
- `$FFCMD=sequencia,HMAC,payload_hex`: HMAC-SHA256 de `nonce|sequencia|payload_hex`.
  Sequência estritamente crescente, consumida mesmo quando GRBL rejeita o comando.
  Payload de 1–200 bytes ASCII imprimíveis; não pode conter vários comandos ou
  bytes realtime brutos. Envelope é validado antes de entrar no parser original.
- Realtime autenticado: marcador binário 0xF8 seguido de
  `sequencia_rt,HMAC,comando_hex\n`, com HMAC de `nonce|rt|sequencia_rt|comando_hex`.
  Tem contador separado e é processado na tarefa de entrada, mesmo quando o
  parser está aguardando uma sondagem pausada. Responde `[FFRT:OK]`/`[FFRT:ERR]`,
  sem roubar o ACK de uma linha G-code pendente.

Estados criptográficos são protegidos por mutex; o mutex é liberado antes de
executar movimentos/sondagens. A autorização transitória é vinculada à tarefa
RTOS e ao transporte, evitando que um handler HTTP concorrente herde a autorização.
A placa **não libera comandos sem assinatura** após autenticar: cada comando de
execução exige seu MAC. Isso evita um desbloqueio global entre USB/Telnet/WebSocket.
Os IDs da base distinguem tipos de transporte, não cada socket; desafios concorrentes
no mesmo tipo podem invalidar a sessão e causar negação de serviço. Não há promessa
de disponibilidade contra outros clientes interferindo.

O reset invalida nonces/contadores e o programa exige reconexão explícita.
Cada nova conexão do programa faz novo desafio. A UART não fornece ao firmware
uma notificação confiável de fechamento do aplicativo; a proteção permanece por
comando, sem depender dessa detecção. Não são repetidos comandos automaticamente
após timeout, falha de escrita ou perda de confirmação.

## O que isso garante e o que não garante

Um sender comum sem a chave consegue configurar parâmetros permitidos, mas não
gerar MACs válidos de execução. O Python confere o firmware esperado e ambos
comprovam posse da chave compartilhada. O BIN publicado contém a chave compartilhada solicitada pelo usuário. O arquivo
fonte gerado com os bytes da chave fica ignorado no Git; isso não impede extrair
a chave do BIN público ou do EXE. Uma extração permite clientes compatíveis
com todas as placas desta edição.

Não autentica o arquivo EXE como identidade inviolável. Copiar a chave possibilita
outro cliente autorizado. O hash reportado por firmware é uma conferência de
compatibilidade; firmware malicioso pode mentir sobre ele. Não é atestação de
hardware. Não há Secure Boot, criptografia de flash/NVS ou transporte criptografado.
Quem regrava a placa fisicamente pode remover o bloqueio. Alterações em eFuses
não foram realizadas. Não usar a rede em ambiente hostil confiando somente nisso.

## Validação e aceitação física

Testes host compilam o FFSTAuth.cpp real com shims de GPIO/RTOS/identidade e OpenSSL
para comparar HMAC com o cliente Python. Verificam recusa de substituição da chave tanto na USB quanto em outro transporte,
comandos sem assinatura, política pública,
MAC alterado, replay de prova/pacote, sequência errada, nonce novo, reset, chave
errada, firmware inesperado, frames realtime e ACKs. O shim não substitui o
parser/máquina completos, mbedTLS do ESP32, pilhas de rede ou drivers reais.

Na bancada, com energia de ferramentas desligada, ainda precisam passar:

1. Programa antigo/terceiro: $$ e $100=valor funcionam com máquina parada; G0,
   G38.2, $H, $J, M3, M8, $N0=... e restauração são bloqueados.
2. Conectar e autenticar sem pareamento: jog, sondagem, edição de configurações
   pelo programa e execução de arquivo funcionam; repetir o teste após reiniciar.
3. Outro sender em paralelo continua sem movimento mesmo com o Python autenticado.
4. Testar pause/resume em movimento e durante G38.x; o resume assinado deve ser
   processado sem esperar o ACK da própria sondagem pausada.
5. Cancelar deve enviar hold/reset sem esperar fila, invalidar a sessão e exigir
   reconexão. Verificar limites, falha de contato e emergência da máquina.
6. Testar temporização, precisão da malha PCB e carga de CPU; HMAC e envelope
   aumentam tráfego/latência, e o envio usa uma linha pendente por vez.
7. Clientes Wi-Fi reais: consultas/configuração permitidas, todos os caminhos de
   execução sem chave bloqueados, reconexão e cliente concorrente. Ainda pendentes.

Compilação/testes host aprovados não validam a integração física. O executável
Windows e a interface Tk não foram executados neste ambiente Linux.

## Reprodução e distribuição da chave fixa

`tools/prepare_shared_key.py` gera a chave uma vez e guarda uma cópia local
ignorada em `.private/shared_key.bin`, além do header gerado também ignorado.
Rebuilds reutilizam esse arquivo. Em outro checkout, o script recupera a chave
do BIN publicado desta edição para reproduzir a mesma família. Se não existir
seed nem BIN com o registro, gera outra chave, portanto não silenciosamente
compatível com placas antigas. Essa capacidade de extração é inerente à escolha
de distribuir o mesmo segredo em todas as placas, não um mecanismo de sigilo.
Nenhum valor da chave é impresso nos logs ou enviado ao chat.
