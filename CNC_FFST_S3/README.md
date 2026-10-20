# CNC_FFST S3 — placa-base para DevKit N16R8, proposta R1

[**Abrir/baixar o PDF da proposta — 5 folhas A3**](artifacts/CNC_FFST_S3_Carrier_Proposta_R1.pdf)

Proposta de esquema funcional para revisão visual: placa-base (carrier) onde serão encaixadas a ESP32-S3 N16R8 dual USB e quatro módulos DRV8825. A USB usada será a da própria ESP32. Não haverá outro conector USB ou conversor USB/serial no carrier.

**Ainda não é esquema liberado para fabricação.** Nesta entrega não há PCB roteada, arquivo KiCad/netlist ou firmware BIN para este hardware.

## Requisitos incorporados

- Placa de desenvolvimento ESP32-S3 N16R8, 16 MB flash / 8 MB PSRAM, duas USBs, encaixável.
- Anúncio informado: https://www.mercadolivre.com.br/p/MLB2069410538
- grblHAL como base, com quatro eixos independentes X/Y/Z/A.
- Quatro DRV8825 StepStick em soquetes 2 × 8.
- Motores em 24 V; NEMA17 informados como 2 A/fase, com ajuste VREF no próprio módulo.
- STEP/DIR em GPIOs diretos, sem I2S, multiplexação ou expansores externos.
- ENABLE comum, com inibição por emergência.
- Uma saída PWM 3,3 V para chave externa entre laser e controlador do spindle.
- Sem display; limites, sonda, emergência, feed hold e cycle start.

O GPIO42 é uma habilitação lógica auxiliar interna do PWM (`TOOL_ARM`), não um ENABLE individual dos drivers nem outro PWM.

## Placa do anúncio e encaixe

O anúncio não pôde ser acessado neste ambiente (HTTP 403). O pinout físico específico, a quantidade de pinos, a distância entre fileiras e a orientação dos conectores **não foram confirmados**. Os desenhos usam nomes GPIO; não são a ordem física dos soquetes.

Antes de desenhar o footprint do encaixe, conferir foto nítida dos dois lados, todas as marcações dos pinos e medidas da placa/distância entre fileiras. A placa-base precisa deixar acesso às USBs, aos botões e à antena da DevKit. Não assumir que clones N16R8 tenham dimensões e circuitos iguais.

Reservados, sem uso externo pela proposta:

- GPIO35/36/37: PSRAM octal na configuração N16R8.
- GPIO19/20: USB nativa da própria placa.
- GPIO43/44: ponte USB/serial da própria placa.
- GPIO38/48: possível LED RGB integrado em diferentes revisões.
- GPIO0/3/45/46: strapping/boot.

`TOOL_ARM` foi movido de GPIO38 para GPIO42 justamente para evitar conflito com o RGB de variantes. Nenhuma entrada/saída ativa da placa-base usa os GPIOs reservados acima. As reservas precisam ser conferidas no modelo real.

## O que o PDF mostra

1. Bloco da DevKit encaixável e tabela de GPIOs propostos.
2. Ligações funcionais dos 16 pinos de cada soquete DRV8825.
3. Alimentação dos primeiros testes e uso da USB/regulador existentes na DevKit.
4. Condicionamento de limites, sonda e comandos por contato seco.
5. ENABLE comum, bloqueio do PWM por emergência e chave seletora externa.

A numeração lógica dos módulos de driver segue `Driver_Motor:Pololu_Breakout_DRV8825` do KiCad. Conferir o módulo DRV8825 real e a orientação física dos soquetes antes do layout. Essa numeração não representa a vista física de inserção.

## Alimentação inicial

A ESP32 será alimentada pela própria USB. O pino 3V3 da DevKit fornecerá apenas a alimentação da lógica do carrier. Na proposta, os rótulos `3V3` e `3V3_DK` representam essa mesma rede.

Os motores usarão fonte separada de 24 V com proteção e GND comum, mantendo os retornos de potência fora dos caminhos sensíveis da lógica. **Não ligar 24 V em 5V, VBUS ou 3V3 da DevKit.** Não foi adicionado conversor 24 V/5 V nem fonte de 5 V externa no carrier desta revisão. A alimentação sem cabo USB precisará de revisão específica, após conferir o circuito da placa real.

Fusível, proteção de inversão, TVS, supervisor, ESD, conectores e suas referências comerciais ainda precisam ser selecionados e dimensionados. São blocos identificados como pendentes, não circuitos prontos para fabricação.

## Firmware e validação ainda pendentes

O driver grblHAL consultado tem geração direta por RMT. Quatro STEP usam os quatro canais TX do S3; o LED endereçável não deve consumir RMT. O mapa S3 genérico tem restrição ao quarto motor: esta placa precisa de mapa próprio.

Ainda faltam mapa grblHAL para esta DevKit, configuração de flash/PSRAM N16R8, firmware compilado, autenticação portada e procedimento de criptografia/proteção específico do S3. Os BINs e o gerenciador anteriores da DLC32 V2.1/ESP32 clássico não devem ser usados nessa placa S3.

## Entradas, PWM e emergência

As entradas propostas são para contato seco/3,3 V, não para sensores de 12/24 V. A saída PWM assume sinal ativo alto e GND compatível com laser e controlador de spindle. A chave externa comuta apenas o sinal, com posição central desligada e ruptura antes do contato. Ela não informa sua posição ao firmware: trocar com máquina parada e ajustar o modo pelo software.

O circuito de potência da emergência é externo e depende das cargas. A placa-base monitora contato auxiliar NC e bloqueia sinais. Não há certificação de segurança nesta proposta. A corrente de fase não é medida pelo ESP32; continua ajustada pelo VREF de cada módulo.

## Arquivos e verificações

- `artifacts/CNC_FFST_S3_Carrier_Proposta_R1.pdf`: proposta de esquema para visualizar.
- `hardware/pinagem_carrier_r1.csv`: GPIOs, sem posições físicas inventadas.
- `hardware/proposta_carrier_r1.json`: escopo e pendências estruturados.
- `tools/gerar_proposta_pdf.py`: fonte da geração vetorial, usando ReportLab e DejaVu.
- `docs/REFERENCIAS.md`: versão do driver consultado e referências para revisão elétrica.

Foram conferidos conflitos da atribuição de GPIOs, reservas de memória/USB e coerência dos pinos dos DRV8825 com a biblioteca local. O PDF foi renderizado e inspecionado visualmente. Não há validação ERC/DRC, simulação de potência, ensaio físico nem validação do anúncio/modelo exato.
