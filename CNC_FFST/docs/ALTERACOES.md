# Alterações sobre o ZIP original

## Plataforma e identificação

- `Firmware/platformio.ini`: alvo padrão `cnc_ffst_v2_1`.
- `Firmware/ini/mks_dlc32.ini`: novo ambiente herdando o alvo cartesiano original,
  TMCStepper fixado em 0.7.3 (versão resolvida pela base), macros CNC_FFST_BUILD,
  CNC_FFST_HEADLESS e FORCE_INITIALIZATION_ALARM. Removido `-w` apenas no perfil
  novo para revelar os avisos originais; demais flags e plataforma 3.2.0 mantidos.
- `Grbl.h`: build próprio `CNC_FFST-0.1.0-test` sob macro; GRBL 1.1 preservado.
- `Report.cpp`: mensagem de identificação adicional no banner, mantendo a linha
  Grbl esperada por senders; `$I` usa a versão própria.
- `Machines/i2s_out_xyz_mks_dlc32.h`: nome de máquina/produto e rótulo de placa
  próprios sob macro. O original chama a variante elétrica V2.x de USE_BOARD_V2_0;
  essa macro foi mantida. Nenhum pino nem default mecânico foi alterado. Na revisão 0.2.0-test,
  o tipo padrão passa a LASER e DEFAULT_LASER_MODE a 1 apenas sob CNC_FFST_BUILD;
  LASER_OUTPUT_PIN é alias de SPINDLE_OUTPUT_PIN (GPIO32). O driver PWM permanece
  disponível para operação de spindle. NVS existente não é migrada automaticamente.

## Sem display e segurança

- `Grbl.cpp`: não inicializa backlight, TFT/DMA, beep, tarefas LVGL/frame no perfil
  headless. Inicializa dados MKS e Wi-Fi sem depender da tarefa de display.
  Não carrega `mkscfg.txt`/modo de teste de fábrica via UI/SD nesse perfil, evitando
  depender de objetos LVGL e bypass de inicialização normal de limites/sonda.
  Configuração por serial/Wi-Fi e NVS continua disponível. Bibliotecas/UI originais
  permanecem nas fontes, mas a tarefa de display não é iniciada.
- `Protocol.cpp`: remove a injeção automática de `$x` apenas no perfil novo.
  O bloqueio inicial é obrigatório; desbloqueio/homing requer ação do operador.
  O reset único legado de inicialização foi preservado.
- `Probe.cpp`: exclui do perfil CNC_FFST o bloco legado de monitor de acidente
  por contato prolongado no pino da sonda. Já estava inativo no original. Nenhuma
  alteração nas quatro funções centrais de sondagem nem no ciclo G38.x.

## Pinagem mantida

| Função | Atribuição original mantida |
| --- | --- |
| Sonda | GPIO22, INPUT_PULLUP, `$6=1` default |
| Laser/spindle PWM | GPIO32, PWM default 1920 Hz |
| Limites X/Y/Z | GPIO36 / GPIO35 / GPIO34 |
| I2S BCK / WS / DATA | GPIO16 / GPIO17 / GPIO21 |
| Disable X/Y/Z | I2SO(0), compartilhado |
| X step / dir | I2SO(1) / I2SO(2) |
| Y step / dir | I2SO(5) / I2SO(6) |
| Z step / dir | I2SO(3) / I2SO(4) |
| Coolant flood | GPIO4 |
| SD SCK/MISO/MOSI/CS/detect | GPIO14/12/13/15/39 |

GPIO34–39 não oferecem pull-up interno no ESP32; verificar circuito da placa e
polaridade reais dos fins de curso. Não foram remapeados pinos LCD para E-stop.
Não há entrada de chama dedicada nem E-stop dedicado nesta definição de máquina.

## Arquivos novos

README_CNC_FFST, documentos de investigação/testes/compilação, patch contra o ZIP,
manifesto de hashes das fontes originais, requisitos Python fixados, build.sh,
check_probe.py e artefatos de compilação. O README e LICENSE upstream permanecem.
O checkout `/workspace/MKS_DLC32` e seu ZIP não foram alterados.

## Compatibilidade e limitações

Movimento, parser, serial, Wi-Fi, drivers de laser/spindle, G38.x e limites
permanecem baseados no código original. Isso foi verificado por comparação de
fontes e compilação; funcionamento físico não foi verificado. Não é uma versão
de produção estável certificada. Não há seleção de ferramentas simultâneas,
novo controle de spindle separado ou compensação de mapa PCB no controlador.

## Revisão 0.2.0-test

Ajuste solicitado para versão laser: perfil LASER/$32=1, alias de pino e versão
própria atualizada. Documentação LASER_SPINDLE.md detalha a configuração persistida,
escala S e seleção física. 0.1.0-test usava o default PWM original e não deve ser
confundida com esta entrega laser.

## Identificação 0.2.0 sem sufixo

A pedido do usuário, removido `-test` da identificação em Grbl.h, Report.cpp e
FW_NAME. Recompilação e reempacotamento do BIN completo; nenhuma mudança de
funcionalidade ou pinagem. O usuário relatou funcionamento da imagem completa;
a remoção do rótulo não representa validação adicional de segurança ou sondagem.

## Revisão 0.3.0 — autenticação solicitada pelo usuário

- FFSTAuth.cpp/.h implementam desafio/resposta HMAC-SHA256, chave fixa comum
  compilada, identidade de firmware, sequência anti-replay e contexto por tarefa/cliente.
- Serial.cpp trata retomada/overrides autenticados fora da fila G-code, mantendo
  parada/reset/status públicos. Buffers de linha de protocolo aumentados a 768.
- ProcessSettings.cpp limita settings e comandos sem assinatura e bloqueia ações
  WebUI/SD assíncronas. Scripts de startup não executam automaticamente.
- GCode.cpp exige contexto autenticado, exceto M5/M9 exatos e linhas vazias.
- Grbl.cpp inicializa o mutex e revoga sessões em reset. Protocol.cpp desabilita
  parking automático para evitar retração disparada sem autenticação.
- Identificação 0.3.0. Pinagem, geometria, algoritmo de sondagem, limites, parser
  e drivers mantidos; as entradas de execução passam pelo novo controle de acesso.
- Python original recebe módulo de transporte, manifesto do BIN e autenticação
  automática ao conectar. Rotinas de geometria/mapa/editor não foram reescritas.
- Novos scripts de geração da chave/header, manifesto e build EXE Windows.
  Header e seed locais não são publicados. BIN público contém chave recuperável.
- A primeira implementação em andamento previa pareamento NVS por placa; foi
  substituída antes da publicação pela chave fixa conforme pedido do usuário.
  Nenhum firmware de pareamento NVS foi entregue como versão final.
