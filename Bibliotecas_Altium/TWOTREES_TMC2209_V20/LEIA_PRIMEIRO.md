# TWOTREES TMC2209 V2.0 — biblioteca de intercâmbio para Altium, revisão A

## Identificação e estado
A foto enviada mostra TWOTREES TMC2209 V2.0, não BIGTREETECH V1.2. As 16 funções dos pinos foram transcritas da foto. Este pacote é um estudo para revisão, NÃO liberado para fabricação. Não houve ensaio no Altium nem medição de um módulo físico.

O formato entregue para símbolo/footprint é EAGLE XML `.lbr`, importável por versões do Altium Designer com EAGLE Importer. NÃO é um arquivo nativo `.SchLib` ou `.PcbLib`. O Import Wizard do Altium gera as bibliotecas nativas. O modelo 3D STEP é independente e deve ser associado após importar.

## Conteúdo
- `TWOTREES_TMC2209_V20.lbr`: símbolo, footprint e associação dos 16 pads.
- `TWOTREES_TMC2209_V20_Completo.step`: módulo com dissipador e dois soquetes fêmea; modelo recomendado para o carrier.
- `TWOTREES_TMC2209_V20_Dissipador.step`: módulo com dissipador, sem soquetes.
- `Soquetes_2x8_12p70mm.step`: soquetes separados.
- `Previa_3D.png`: render da geometria STEP, com dissipador azul e espaçadores vermelhos.
- `Footprint_1para1.pdf`: gabarito nominal em escala 1:1 para impressão/conferência.
- `Footprint_mecanico.dxf`: auxílio de desenho; NÃO tem associação elétrica.
- `pinagem.csv`, `dimensoes.json`: definição dos pads e hipóteses mecânicas.
- `render_blender.py`: renderização opcional da prévia em Blender/Cycles.
- `gerar.py`: fonte regenerável com Python/CadQuery 2.7; Blender para a prévia; `complementar.py`: fonte dos auxiliares (ReportLab/ezdxf).

## Importar no Altium
1. Descompacte o ZIP inteiro.
2. Abra File > Import Wizard e selecione EAGLE Designs and Libraries (nome pode variar por versão). Se não aparecer, habilite o importador EAGLE em Extensions and Updates.
3. Selecione `TWOTREES_TMC2209_V20.lbr` como biblioteca e finalize a conversão. Confira os relatórios do importador e salve `.SchLib`/`.PcbLib` resultantes.
4. Abra o footprint na PcbLib. Place > 3D Body > Generic 3D Model/Embed STEP e escolha `TWOTREES_TMC2209_V20_Completo.step`.
5. O STEP já usa o topo da PCB do carrier como Z=0. Comece com rotação XYZ=0 e deslocamento XYZ=0; confira a origem importada pelos centros dos furos. Não acrescente novamente a altura do soquete.
6. Inspecione em 3D (tecla 3), confira EN/VM, a correspondência dos 16 pads e as folgas antes de associar ao esquemático.
7. Compile/valide a biblioteca no Altium e imprima o gabarito 1:1. Não presumir que uma conversão sem erro certifica o encaixe.

## Orientação e numeração própria
Vista superior do carrier, módulo encaixado, extremidade EN/VM voltada para +Y:

```
       EN 1           9 VM
      MS1 2          10 GND_POWER
      MS2 3          11 M1B
      PDN 4          12 M1A
    USART 5          13 M2A
      CLK 6          14 M2B
     STEP 7          15 VIO
      DIR 8          16 GND_LOGIC
```

A foto do anúncio está girada 180 graus em relação a essa vista. As designações 1–16 são próprias desta biblioteca; não são os números do CI TMC2209 e não são a numeração Pololu/DRV8825 de outras bibliotecas. PDN e USART ficam separados: a foto não prova suas ligações internas. Não unimos esses pinos no símbolo. Não foi criada conexão DIAG/INDEX ausente no encaixe mostrado.

## Dimensões: nominais/estimadas, conferir no módulo real
- Duas fileiras de oito contatos; passo longitudinal nominal 2,54 mm.
- Distância nominal entre fileiras 12,70 mm. Confirmar no módulo e na DLC32 real.
- PCB estimada 15,24 × 20,32 × 1,60 mm; centro XY=(0,0).
- Furos do carrier propostos 1,00 mm e pads 1,90 mm. Conferir a ficha do soquete escolhido.
- Corpo do soquete estimado 7,00 mm; face inferior da PCB do módulo Z=8,50 mm.
- Dissipador ilustrativo azul 9,00 × 10,50 mm, base 1,00 mm + aletas 11,00 mm. Altura total aproximada acima do carrier: 22,315 mm.
- Aparência, alturas do dissipador, posições dos passivos e trimpot são estimadas da foto, NÃO modelo CAD oficial do fabricante. O STEP não é uma digitalização dimensional do produto.

## Compatibilidade com MKS DLC32
O encaixe StepStick é apenas compatibilidade mecânica nominal; NÃO significa substituição elétrica irrestrita de DRV8825. VIO ocupa uma posição com outra função em determinados drivers, e PDN/USART/CLK não são RESET/SLEEP/M2 equivalentes. Confira redes e jumpers da revisão exata da DLC32 antes de inserir. Não conecte VIO a 24 V, não reutilize indiscriminadamente os jumpers de microstep e não una duas saídas.

A biblioteca não implementa UART no firmware nem define corrente/VREF. O desenho da placa-base anterior usava DRV8825; esta entrega não altera automaticamente aquele circuito.

Fonte de identificação/pinagem: fotos fornecidas pelo usuário do anúncio https://pt.aliexpress.com/item/1005010646278731.html (acesso automatizado bloqueado). As medidas StepStick são hipóteses nominais a conferir. Nenhum documento BIGTREETECH foi usado para declarar medidas TWOTREES verificadas.
