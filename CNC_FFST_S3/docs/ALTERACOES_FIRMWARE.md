# Alterações CNC_FFST-S3 0.1.0

Base: grblHAL ESP32 `0b2d3e1bb7da3b0ae0e03490b71275374eb84c67`, core `4ec1ae44b857a70d2f9298344feac4b43ed0eb6b` (GRBL_VERSION 1.1f, build 20261015). Demais submódulos em `firmware/source.lock.json`; licenças originais preservadas. Este projeto é separado do firmware ESP32 clássico da DLC32.

- `platformio.ini`, defaults sdkconfig e tabela de partições: ESP32-S3 N16R8, flash DIO 16 MB, PSRAM octal 8 MB; perfis USB/UART e USB nativa. PlatformIO 6.1.18, espressif32 5.3.0, ESP-IDF 4.4.3. Dependências Python fixadas em tools/requirements-build.txt.
- Mapa `main/boards/my_machine_map.h`: quatro STEP/DIR diretos; ENABLE comum, PWM13 e TOOL_ARM42. Mesmos GPIOs da proposta R2. Nenhuma multiplexação I2S. RGB desativado para reservar os quatro canais RMT aos motores.
- `main/main.c`: inicialização antecipada do ENABLE inativo, STEP/PWM/TOOL_ARM baixos.
- `main/driver.c`: ENABLE comum considera qualquer eixo solicitado, inclusive movimento só do A.
- Pulsos STEP de 5 us e atraso DIR/STEP de 2 us para DRV8825. Conferir com osciloscópio antes de ajustar velocidades. Valores mecânicos de passos/mm, aceleração, curso e velocidade requerem calibração da máquina.
- Limites NC invertidos (máscara 15), emergência ativa alta, probe NO ativo alto: dependem do condicionamento externo da proposta, não de ligação arbitrária à DevKit. Proteções e estados de alarme originais continuam presentes.
- `main/ffst_auth.c/.h`: protocolo HMAC v1 e credencial comum compatível com o projeto anterior, identidade vinculada ao hash da aplicação, nonce aleatório renovado após reset, sequências separadas para comandos e realtime. Handshake não libera G-code sem assinatura. Paradas/status/reset públicos, retomada protegida. Configuração pública limitada a lista explícita em estado permitido.
- Guardas nos pontos de execução do core (`gcode.c`, `system.c`, `protocol.c`): comandos recebidos durante probe/homing não herdam autorização de um comando assinado em execução. Autorização vinculada à tarefa; processamento criptográfico fora das interrupções. Startup automático de G-code desabilitado.
- Saída laser PWM sem direção; o mesmo PWM atende as duas ferramentas. Chave externa seleciona alimentação; firmware não lê sua posição. Modo laser inicialmente ativo; selecionar corretamente modo/ferramenta com máquina parada. Sinal de emergência não substitui corte externo de energia.
- Sem sensor FIRE/FLAME neste mapa; nenhum alarme desse sensor é incluído. Isso não valida sondagem física ou segurança das ferramentas.
- Wi-Fi, Bluetooth, SD, WebUI e coolant desabilitados nesta primeira versão USB. Removidos embeddings de HTML/favicon não utilizados no CMake.
- `python/`: cliente único gerado por perfil, autenticação e BIN correspondentes embutidos. Interface PCB mantém XYZ; aceita relatório PRB de quatro coordenadas preservando XYZ. Eixo A disponível por G-code assinado; não há novo painel de jog A.
- Ferramentas de build, empacotamento e diagnóstico somente leitura. Imagem única 16 MB no offset 0x0; valida chip, checksums, hash, memória e credencial. Pré-build recupera a credencial do BIN fornecido se faltar o seed local, sem criar chave diferente.

## Segurança e escopo

Este BIN de bancada **não ativa flash encryption, Secure Boot nem grava eFuses**. A autenticação não impede extração do BIN ou da chave comum. O diagnóstico ajuda a planejar provisionamento futuro por placa, mas não implementa essa proteção. A chave HMAC compartilhada não é uma chave de criptografia da flash. O procedimento de proteção do S3 requer relatório da placa real e uma entrega própria antes de qualquer operação irreversível.

## Compilação e verificações

Os dois perfis finais compilaram com sucesso. Cada compilação registrou um aviso herdado de `main/grbl/stream_json.c:251`: variável `c` atribuída mas não utilizada. Nenhum erro na compilação final.

Falhas iniciais corrigidas: caminho de geração do favicon no CMake (recurso não usado removido); `tinyusb.h` ausente no perfil nativo (habilitada opção pai CONFIG_TINYUSB). Alguns mirrors de dependências retornaram HTTP 403; o PlatformIO obteve os pacotes em mirror alternativo com verificação preservada. Logs mantidos em `artifacts/validation/`.

17 testes de autenticação passaram no computador, incluindo replay, bypass por G-code cru, realtime, reset, sondagem assinada, limites de configuração e alarmes. Testes de interface Tk passaram para os dois perfis e integração com Montador de Páginas. São testes simulados com o módulo C real de autenticação, não ensaios na ESP32. Empacotamento verifica a imagem completa e a correspondência com o cliente.

**Não foram validados em hardware:** boot N16R8, portas USB reais, tempos STEP/DIR, movimento XYZA, limites, emergência, laser/spindle, sondagem elétrica, falha de sondagem ou proteção de leitura. Testar inicialmente sem energia nas ferramentas e sem motores, conforme FIRMWARE_S3.md.
