# Referências da proposta R2

## grblHAL

Driver ESP32, commit consultado: `0b2d3e1bb7da3b0ae0e03490b71275374eb84c67`.
Core indicado pelo submódulo nessa revisão: `4ec1ae44b857a70d2f9298344feac4b43ed0eb6b`.

- Repositório: https://github.com/grblHAL/ESP32
- Pulsos diretos por RMT e ENABLE comum: https://github.com/grblHAL/ESP32/blob/0b2d3e1bb7da3b0ae0e03490b71275374eb84c67/main/driver.c
- Mapa S3 genérico, com restrição ao quarto motor: https://github.com/grblHAL/ESP32/blob/0b2d3e1bb7da3b0ae0e03490b71275374eb84c67/main/boards/generic_s3_map.h
- Conflito de LED endereçável RMT com quarto motor: https://github.com/grblHAL/ESP32/blob/0b2d3e1bb7da3b0ae0e03490b71275374eb84c67/main/neopixel_rmt.c

O mapa genérico não é um perfil pronto desta placa: é necessária adaptação própria. Nenhuma compilação grblHAL foi executada para a proposta R2.

## Bibliotecas EDA e fabricantes

Símbolos locais do KiCad 9.0.2 usados para conferir numeração lógica:

- `RF_Module:ESP32-S3-WROOM-1`, somente como referência do módulo; não define o conector da DevKit N16R8;
- `Driver_Motor:Pololu_Breakout_DRV8825`.

Referências para revisão elétrica e seleção de peças:

- ESP32-S3-WROOM-1 / WROOM-1U: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
- GPIO ESP32-S3: https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/peripherals/gpio.html
- DRV8825: https://www.ti.com/lit/ds/symlink/drv8825.pdf
- Carrier DRV8825 Pololu: https://www.pololu.com/product/2982

A proposta não pressupõe que todo módulo vendido como DRV8825 tenha a mesma implementação, resistência Rsense ou capacidade térmica. Conferir os módulos reais antes de definir footprint, orientação e VREF. Os datasheets vinculados devem ser consultados na revisão elétrica; não foram baixados neste ambiente.

## DevKit encaixável

Anúncio do usuário: https://www.mercadolivre.com.br/p/MLB2069410538

Acesso bloqueado por HTTP 403. Não foi confirmado o modelo/revisão nem seu pinout físico. A proposta usa identificações GPIO e preserva USBs, PSRAM octal e os dois GPIOs usuais de RGB (38/48), aguardando fotos e medidas da unidade real.
