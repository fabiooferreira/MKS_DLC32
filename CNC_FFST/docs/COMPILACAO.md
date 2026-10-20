# Compilação e verificações

Compilação do alvo laser CNC_FFST 0.2.0-test: SUCCESS, 32,11 s; 0 erros, 236 ocorrências de warning. Alteração de header de máquina recompilou os dependentes; bibliotecas válidas foram reutilizadas.
RAM: 64420/327680 bytes; flash: 1691362/3145728 bytes.
Base original: SUCCESS, 86,14 s, flags originais incluem -w e ocultam avisos.
A revisão anterior 0.1.0-test teve repetição incremental via tools/build.sh: SUCCESS, 3,93 s. A revisão laser foi compilada pelo mesmo script.

## Avisos encontrados (agrupados por mensagem)

| Ocorrências | Mensagem |
| --- | --- |
| 28 | `"TOUCH_CS" redefined` |
| 28 | `narrowing conversion of '(((int)b) >> 3)' from 'int' to 'uint16_t {aka short unsigned int}' inside { } [-Wnarrowing]` |
| 28 | `narrowing conversion of '(((int)g) >> 2)' from 'int' to 'uint16_t {aka short unsigned int}' inside { } [-Wnarrowing]` |
| 28 | `narrowing conversion of '(((int)r) >> 3)' from 'int' to 'uint16_t {aka short unsigned int}' inside { } [-Wnarrowing]` |
| 2 | `no return statement in function returning non-void [-Wreturn-type]` |
| 8 | `control reaches end of non-void function [-Wreturn-type]` |
| 1 | `extra tokens at end of #endif directive [-Wendif-labels]` |
| 1 | `variable 'pwm_value' set but not used [-Wunused-but-set-variable]` |
| 95 | `ISO C++ forbids converting a string constant to 'char*' [-Wwrite-strings]` |
| 2 | `suggest parentheses around assignment used as truth value [-Wparentheses]` |
| 1 | `enumeration value 'PROBE_FINISH' not handled in switch [-Wswitch]` |
| 1 | `'speed' may be used uninitialized in this function [-Wmaybe-uninitialized]` |
| 1 | `'step' may be used uninitialized in this function [-Wmaybe-uninitialized]` |
| 12 | `cast from pointer to integer of different size [-Wpointer-to-int-cast]` |

Todos os locais e repetições estão em artifacts/warnings.txt; o contexto integral está em artifacts/build-full.log.
Não foram ocultados os avisos no perfil novo. Tratam-se de código herdado não corrigido nesta entrega; não é correto declarar ausência de riscos com base na compilação. Avisos de retorno ausente, variáveis possivelmente não inicializadas, malloc implícito e ponteiros merecem auditoria antes de produção. A maioria das repetições vem de headers LVGL incluídos em vários arquivos.

## Verificações adicionais

- Testes host de Probe.cpp: 8 combinações de nível, polaridade e direção, captura de posição, cancelamento, inicialização pull-up e estado sem pino; passaram. Não testam hardware/ISR real.
- ELF contém probe_get_state, probe_state_monitor e limits_init; não contém símbolos mks_probe_check, mks_probe_init ou lvgl_disp_task.
- Caminhos MotionControl.cpp, Stepper.cpp, Limits.cpp, System.cpp, GCode.cpp e drivers de spindle permanecem byte a byte iguais ao ZIP original.
- A imagem e seus checksums foram examinados com esptool image_info; resultado salvo em artifacts/image-info.txt.
- Nenhum teste serial/Wi-Fi real, movimentação, gravação, sondagem, FIRE ou emergência foi executado na placa.

## Diagnóstico da ferramenta de inspeção

A primeira tentativa de image_info usou o Python global e falhou por ausência de pyserial. A invocação correta usa o Python do venv do PlatformIO; essa correção não alterou firmware ou dependências do projeto. Depois, a inspeção sem `--chip esp32` tentou o formato padrão ESP8266 e falhou na leitura dos segmentos. Com `--chip esp32`, a imagem ESP32 foi reconhecida e checksum/hash internos resultaram válidos; não foi necessário regenerar o BIN.

Revisão laser: driver LASER e macro LASER_OUTPUT_PIN=GPIO32 confirmados nas fontes, `$32=1` por default. Configuração NVS existente não é substituída pela gravação. Teste de driver/modo em hardware continua pendente.

## Recompilação da identificação 0.2.0

Removido o sufixo -test conforme pedido. Build e imagem completa gerados com sucesso; 236 ocorrências de warning nesta execução, 0 erros. Logs atuais em artifacts/build.log e artifacts/full-image-build.log; identificação verificada nos bytes da aplicação. Nenhuma mudança de lógica.
