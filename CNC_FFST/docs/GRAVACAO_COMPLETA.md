# Imagem completa de flash para teste — CNC_FFST 0.2.0

`artifacts/CNC_FFST_0.2.0_FULL_4MB.bin` é uma imagem completa de 4 MB,
com base/endereço de gravação **0x0**. Não confundir com `artifacts/firmware.bin`,
que é somente a aplicação para **0x10000**.

Foi criada com esptool 4.8.1 a partir dos componentes do próprio build
PlatformIO. Não contém código, NVS, credenciais ou SPIFFS extraídos do BIN MKS
fornecido pelo usuário. O BIN MKS serviu apenas para comparar o layout:

| Região | Offset | Conteúdo da imagem CNC_FFST |
| --- | --- | --- |
| Bootloader | 0x1000 | Arduino ESP32 1.0.6, dout/80 MHz, fornecido pelo framework |
| Partições | 0x8000 | huge_app: mesmo layout do BIN MKS analisado |
| NVS | 0x9000 | Vazia, preenchida com FF |
| Dados OTA | 0xe000 | boot_app0.bin do framework |
| app0 | 0x10000 | CNC_FFST 0.2.0 laser, compilado anteriormente |
| SPIFFS | 0x310000 | Vazio, preenchido com FF |

## Antes de gravar

Desconectar alimentação do laser e do spindle. Preservar um backup completo
da flash e registrar calibrações/configurações se ainda houver acesso.
**Gravar a imagem completa sobrescreve NVS e SPIFFS**, incluindo calibração,
configurações Wi-Fi e arquivos de interface web existentes. O preenchimento
vazio não preserva as configurações da placa. Não acrescentar um erase geral
como tentativa de corrigir resets sem necessidade.

## MKSLaserTool

Selecionar a imagem com nome **FULL_4MB**, nunca o BIN de aplicação para um
procedimento de gravação completa. Usar somente se a ferramenta gravar imagens
completas a partir de **0x0**, como o BIN MKS fornecido; conferir a versão e as
opções da ferramenta. O comportamento específico do MKSLaserTool do usuário
ainda não foi observado nem validado. Se não houver como confirmar o endereço,
usar esptool com endereço explícito em vez de adivinhar.

## Alternativa com endereço explícito

Com Python/esptool 4.8.1 instalados no computador conectado à placa, trocar
PORTA pela porta real e executar a partir da pasta que contém o BIN:

```text
python -m esptool --chip esp32 --port PORTA --baud 115200 write_flash 0x0 CNC_FFST_0.2.0_FULL_4MB.bin
```

Após gravar, capturar boot em 115200 baud com a ferramenta sem energia.
Esperado: identificação CNC_FFST e ALARM inicial. ALARM de partida não é reset:
não desbloquear até conferir sinais/configuração. Recalibrar antes de mover.
Se houver reinícios repetidos, interromper o teste e enviar log completo desde
`rst:` até `Backtrace`, `Brownout` ou próximo reset. Não declarar resolvido só
porque a escrita da flash terminou.

O formato completo resolve a diferença de empacotamento encontrada, mas não
prova que esse era o motivo dos resets. O código de aplicação desta imagem é
o mesmo da revisão 0.2.0; não foi feita correção especulativa de runtime.
Sondagem, FIRE, laser, limites e emergência permanecem sem validação física.

Reprodução: `bash tools/build-full.sh`. Logs da mesclagem/verificações e hashes
ficam em artifacts. Não foram executadas operações de gravação neste ambiente.
