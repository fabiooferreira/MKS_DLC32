# CNC_FFST-S3 0.1.0 — firmware inicial para bancada

Alvo: **ESP32-S3 N16R8, 16 MB de flash / 8 MB de PSRAM octal**, na placa-base proposta R2. Sem display, DRV8825 encaixáveis, XYZA, STEP/DIR diretos, ENABLE comum e PWM 3,3 V ligado simultaneamente ao laser e ao controlador do spindle. A chave externa seleciona a alimentação das ferramentas.

**Não usar na DLC32 V2.1/ESP32 clássico ou na DLC32 MAX.** São outros hardwares e pinagens. O anúncio da DevKit não pôde ser verificado: conferir as marcações dos GPIOs antes de ligar qualquer carga. As posições físicas dos soquetes ainda não estão definidas.

Esta é uma versão compilada para ensaios controlados. Não houve teste de boot na placa real, medição de pulsos, movimento, sondagem, segurança, USB físico ou PSRAM real. Os BINs não ativam criptografia nem Secure Boot e não gravam eFuses; **a proteção contra leitura solicitada continua pendente**. Wi-Fi/BLE, WebUI, SD e macros autônomas não foram habilitados nesta primeira versão por USB.

## Base e versões

- grblHAL core 1.1f, build 20261015, commit `4ec1ae44b857a70d2f9298344feac4b43ed0eb6b`.
- Driver ESP32, commit `0b2d3e1bb7da3b0ae0e03490b71275374eb84c67`.
- PlatformIO 6.1.18; espressif32 5.3.0; ESP-IDF 4.4.3.
- Xtensa ESP32-S3 8.4.0+2021r2-patch5; esptool 4.8.1 no empacotamento.
- Fontes de driver, core e submódulos incluídas em `firmware/`, com licenças preservadas e commits em `firmware/source.lock.json`.

A base ESP-IDF é a versão compatível com os caminhos usados pelo driver consultado. A compilação desta versão de bancada não constitui aprovação dessa base para produção/proteção. Uma configuração de produção precisa de revisão de segurança, atualização compatível da base e provisionamento próprio.

## Escolher a USB e o pacote correspondente

| Pacote | Comunicação após o boot | Ambiente PlatformIO |
| --- | --- | --- |
| UART — recomendado para começar | USB/serial integrada à DevKit, ligada aos GPIO43/44 | `cnc_ffst_s3_n16r8_uart` |
| USB nativa | USB OTG da DevKit, GPIO19/20 | `cnc_ffst_s3_n16r8_usb` |

Baud da comunicação GRBL: 115200. A identificação impressa nos conectores e o driver do sistema operacional dependem do clone. Não presumir que as duas portas sejam intercambiáveis durante a execução. A ROM pode permitir gravação por uma porta na qual o firmware escolhido não oferece comunicação depois do boot.

Cada pacote tem seu BIN completo e seu `CNC_FFST_Unico.py`. **Não misturar o Python de UART com o BIN de USB nativa:** os hashes das aplicações diferem. O cliente verifica a imagem exata e não possui fallback para movimento sem autenticação. Use o programa novo mesmo que já tenha o Python 0.3.0 da DLC32 funcionando.

A interface mantém controles de PCB/XYZ. O firmware aceita A por G-code autenticado, mas a interface não ganhou controles dedicados de jog/calibração do eixo A nesta entrega. Não há nova calibração mecânica embutida; configurar passos, velocidades, aceleração e curso antes de movimentar.

## Arquivos de cada pacote

- `CNC_FFST_S3_0.1.0_UART_FULL_16MB.bin` ou `...USB_FULL_16MB.bin`: **arquivo único completo de 16.777.216 bytes, para endereço 0x0**.
- `CNC_FFST_Unico.py`: cliente em um único arquivo, com credencial e identidade da imagem correspondentes embutidas.
- `manifest.json` / `firmware_identity.json` / `SHA256SUMS`: identificação e hashes.
- `LEIA_PRIMEIRO.md` e logs: instruções, avisos e limites.

No projeto completo também há a aplicação separada `firmware_app_0x10000.bin`, bootloader, tabela de partições, ELF e `sdkconfig.used` em `artifacts/UART` e `artifacts/USB`. **A aplicação separada não deve ser gravada em 0x0.** O layout S3 começa com bootloader em 0x0, não em 0x1000 como no ESP32 clássico.

## Gravar no Windows

Instalar Python 3.12. Extrair um dos pacotes em uma pasta e abrir PowerShell nela. Instalar as ferramentas:

```powershell
py -3.12 -m pip install esptool==4.8.1 bitstring==4.3.1 pyserial==3.5 pillow==11.3.0
```

Primeiro testar só a DevKit, sem motores e com laser/spindle fisicamente sem energia. Fechar outros programas usando a porta. Usar o conector adequado e substituir `COM7` pela porta real:

```powershell
py -3.12 -m esptool --chip esp32s3 --port COM7 chip_id
py -3.12 -m esptool --chip esp32s3 --port COM7 flash_id
```

Se não for ESP32-S3 com 16 MB, não gravar este pacote. Se não entrar em download automaticamente, usar BOOT/RESET da própria placa conforme seu fabricante.

Para o pacote UART:

```powershell
py -3.12 -m esptool --chip esp32s3 --port COM7 write_flash --flash_mode keep --flash_freq keep --flash_size keep 0x0 CNC_FFST_S3_0.1.0_UART_FULL_16MB.bin
py -3.12 -m esptool --chip esp32s3 --port COM7 verify_flash 0x0 CNC_FFST_S3_0.1.0_UART_FULL_16MB.bin
py -3.12 CNC_FFST_Unico.py
```

Para USB nativa, usar os mesmos comandos com o arquivo `...USB_FULL_16MB.bin` e o Python da pasta USB. Não usar `--force`, não tentar contornar eFuses existentes e não usar o gerenciador anterior da DLC32 clássica para gravar o S3.

O BIN completo substitui NVS, configurações, dados e arquivos existentes. Preservar seus dados antes de atualizar uma placa em uso. Estes comandos não ativam proteção contra leitura.

Para gerar EXE no seu Windows, a partir do Python correspondente:

```powershell
py -3.12 -m pip install pyinstaller==6.16.0
py -3.12 -m PyInstaller --onefile --windowed --name CNC_FFST_S3 CNC_FFST_Unico.py
```

O EXE não foi gerado nem testado neste ambiente Linux. O arquivo único Python foi testado com o Montador de Páginas original, usando uma placa simulada.

## Pinagem R2 e estados de entrada

| Função | GPIO |
| --- | --- |
| STEP X/Y/Z/A | 4 / 5 / 6 / 7 |
| DIR X/Y/Z/A | 8 / 9 / 10 / 11 |
| ENABLE comum, ativo baixo | 12 |
| PWM compartilhado | 13 |
| TOOL_ARM, habilitação lógica do PWM | 42 |
| Limites X/Y/Z/A | 1 / 2 / 14 / 15 |
| Sonda | 16 |
| Emergência ativa alta | 17 |
| Feed hold / cycle start | 39 / 40 |

A pinagem supõe o condicionamento com inversores Schmitt do PDF R2. Não ligar contatos diretamente e presumir as mesmas polaridades. Com a placa-base:

- Limites NC: normal fechado gera GPIO alto; acionamento/cabo rompido gera baixo. Máscara de inversão padrão 15.
- Sonda NO: sem contato gera GPIO baixo; contato com GND antes do inversor gera GPIO alto. Inversão padrão 0.
- Emergência: normal gera GPIO17 baixo; acionamento/cabo rompido gera alto. `ESTOP_ENABLE=1`, não somente um reset comum.
- Feed hold/cycle start: inativos baixos; botão NO ativo alto após o inversor.
- ENABLE comum: GPIO alto desabilita; qualquer eixo solicitado, inclusive A sozinho, habilita o mesmo /EN.

A DevKit sozinha não fornece esses estados. Entradas com pull-up podem indicar emergência ou sonda ativa. Não desabilitar proteções para ocultar isso: montar o condicionamento ou usar uma bancada controlada que forneça níveis inativos conhecidos, sem cargas.

GPIOs reservados de memória, USBs, straps e RGB não foram usados para os drivers. Pulsos padrão de 5 µs e atraso de 2 µs entre direção e pulso ($29); nenhum I2S, multiplexador ou expansor externo foi acrescentado.

## Autenticação e segurança funcional

Mantido protocolo FFST HMAC v1: `$FFINFO`, `$FFHELLO`, `$FFAUTH`, `$FFCMD` e quadros realtime 0xF8. Mesma credencial compartilhada já escolhida para suas placas. A prova é vinculada ao hash da aplicação, com nonce novo e sequências contra repetição. A chave de autenticação não é uma chave de criptografia da flash.

Movimento, A, homing, jog, sondagem e ferramentas exigem comando assinado. A autenticação não libera globalmente G-code cru. Retomada e overrides exigem assinatura, inclusive o comando estendido de retomada 0x81. Status, reset e comandos de parada continuam acessíveis sem assinatura. Consultas e calibrações permitidas continuam disponíveis a outros programas quando parado e com ferramenta desligada.

Comandos crus recebidos durante uma sondagem/hold não herdam a autorização do comando longo em execução. A verificação HMAC de realtime ocorre fora da ISR. Reset e troca de stream invalidam a sessão. Scripts de inicialização não são executados automaticamente.

Boot em alarme, sem `$X` ou homing automáticos. Hard limits habilitados por padrão, incluindo A. Proteções de emergência e falha G38.2 permanecem no core. Soft limits e homing precisam de configuração mecânica correta; não foram preenchidos cursos e passos fictícios para sua máquina. Não existe sensor FIRE/FLAME mapeado neste hardware. Isso não valida ruído da sonda nem o circuito real.

A emergência física precisa bloquear os sinais e cortar energia independentemente do software, conforme o PDF. O PWM fica nas duas entradas; validar retroalimentação de módulos sem alimentação. A chave de alimentação não informa ao firmware qual ferramenta está selecionada: ajustar modo laser/spindle no software e trocar somente parado com M5/S0.

## Compilar localmente

Baixar o ZIP completo das fontes. Abrir a pasta `CNC_FFST_S3`:

```powershell
py -3.12 -m venv .venv-build
.\.venv-build\Scripts\python.exe -m pip install -r tools\requirements-build.txt
.\.venv-build\Scripts\python.exe tools\build_firmware.py uart
# Ou: usb / all
```

O script usa `.platformio-core` como cache, não grava a placa e não altera eFuses. Se definir `PLATFORMIO_CORE_DIR`, ele é respeitado. Primeiro uso precisa de internet. Códigos-fonte dos submódulos já estão incluídos; não é necessário obter branches atuais da internet.

O pre-hook reaproveita `.private/shared_key.bin` ou recupera o registro do BIN UART distribuído. Se faltar a credencial existente, a compilação falha em vez de criar outra. Não publicar a pasta `.private` nem o header gerado separadamente.

O empacotamento verifica alvo S3, checksum/SHA256 interno, configuração N16R8 e conteúdo da imagem completa. Recusa configurações com Secure Boot/criptografia ativados, pois este fluxo não é um provisionador de produção. Gera BIN e Python correspondentes. Recompilação pode mudar a identidade da aplicação; usar o Python novo.

## Proteção contra leitura: etapa posterior

Não foi substituída por vínculo ao MAC. Para preparar o provisionamento protegido, o projeto inclui uma consulta específica de S3, sem leitura do firmware ou blocos de chave:

```powershell
.\.venv-build\Scripts\python.exe tools\diagnostico_s3.py COM7 --out relatorio_s3.json
```

Fechar o controlador e manter a máquina parada: a consulta pode reiniciar a placa. O JSON contém chip, MAC, flash e campos públicos selecionados de segurança. Enviar esse relatório para avaliar revisão/eFuses e planejar atualização/recuperação. O script não queima eFuses.

Faltam relatório real, configuração de produção/bootloader protegido, chaves de criptografia por dispositivo e validação física do processo. Não usar estes BINs como se já impedissem extração.

## Verificações e logs

Duas compilações passaram, UART e USB nativa. Testes do adaptador C real executados no host usam HMAC por OpenSSL e mocks de HAL/RTOS; não simulam a eletrônica nem o motor. A interface Tk foi testada com o cliente gerado para os dois perfis e com a aplicação de duas páginas produzida pelo Montador original. Uma resposta `[PRB]` com quatro eixos foi recebida e convertida para XYZ na interface PCB.

Os logs completos, incluindo falhas iniciais corrigidas e avisos, estão em `artifacts/validation/`. Falhas corrigidas: recursos HTML embutidos não necessários causavam erro de caminho no PlatformIO; USB nativa exigia habilitar o componente TinyUSB no sdkconfig. Um mirror de pacotes negou acesso e o próprio PlatformIO completou por outro mirror, sem desabilitar verificação.

Os ensaios reais de boot, movimento, laser/spindle, limites, emergência, perda de comunicação e sondagem continuam obrigatórios para validar o firmware na sua placa. Nenhum teste de host deve ser tratado como validação física de segurança.
