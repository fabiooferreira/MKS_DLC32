# TWOTREES TMC2209 V2.0 — bibliotecas NATIVAS Altium, revisão B

## Abrir no Altium Designer
1. Descompacte o ZIP em uma pasta local.
2. Abra `TWOTREES_TMC2209_V20.PcbLib` e `TWOTREES_TMC2209_V20.SchLib` diretamente pelo File > Open. Não é necessário Import Wizard nem EAGLE.
3. Na PcbLib selecione `TWOTREES_TMC2209_V20_2X8` e pressione 3 para visualizar o corpo 3D. O STEP do módulo, dissipador azul e soquetes já está incorporado. Não precisa associar novamente o arquivo STEP externo.
4. Na SchLib selecione `TWOTREES_TMC2209_V20`. A implementação PCBLIB aponta para o footprint acima, com mapeamento 1:1 dos 16 pinos. Instale ambas as bibliotecas nas bibliotecas disponíveis do seu projeto/Altium para resolver o footprint.
5. Confira orientação EN/VM, redes, dimensões e relatórios no seu Altium antes de fabricar.

## O que foi verificado
Os arquivos têm formato binário nativo OLE/Compound File, não são arquivos EAGLE renomeados. Foram gravados e reabertos com OriginalCircuit.Altium (AltiumSharp); verificados 16 pinos/pads, posições, furo 1 mm, camada Multi-Layer e modelo de footprint do símbolo. O STEP incorporado foi extraído por um leitor OLE independente e comparado byte a byte com o original. Veja VALIDACAO_NATIVA.txt.

Não foi possível abrir a interface do Altium neste ambiente: compatibilidade com a sua versão e aparência na interface ainda precisam ser conferidas. O modelo 3D é geométrico aproximado, não CAD oficial TWOTREES. A pinagem segue a foto fornecida, com PDN e USART separados; não foram presumidas ligações internas.

## Dimensões nominais/estimadas
Encaixe 2 fileiras de 8, passo 2,54 mm, entre fileiras 12,70 mm; placa estimada 15,24 x 20,32 mm. Furos propostos 1,00 mm, pads 1,90 mm. Os soquetes têm corpo estimado 7 mm; fundo da PCB do módulo em Z=8,5 mm. Topo do dissipador em Z=22,315 mm, relativo ao topo do carrier (Z=0). Conferir tudo no módulo/soquete físico; imprimir o gabarito em 100%.

Numeração própria, vista superior, EN/VM em +Y:

```
 EN_N  1     9 VM
 MS1   2    10 GND_POWER
 MS2   3    11 M1B
 PDN   4    12 M1A
 USART 5    13 M2A
 CLK   6    14 M2B
 STEP  7    15 VIO
 DIR   8    16 GND_LOGIC
```

A numeração não é a do CI ou da biblioteca DRV8825 anterior. A foto foi rotacionada 180 graus para essa orientação. Compatibilidade mecânica nominal com StepStick/MKS não garante substituição elétrica: conferir VIO, PDN, USART, CLK e jumpers da DLC32 antes de energizar. Esta entrega não altera o firmware ou o esquema da placa-base.

## Fontes e reprodução
Gerador próprio em `Generator/Program.cs`. Ele usa OriginalCircuit.Altium/AltiumSharp, MIT, commit ce72437f30cd54f549601d4e0ca5846d21272150: https://github.com/issus/AltiumSharp . Licença em Generator/ALTIUMSHARP_LICENSE.txt.

Para reproduzir: .NET SDK 10, clonar o commit acima, inicializar submódulo `shared/OriginalCircuit.Eda.Abstractions`, e atualizar apenas o Microsoft.SourceLink.GitHub do Directory.Build.props de 8.0.0 para 10.0.403. Essa atualização evita uma dependência de build com alerta NU1902; não altera o escritor de bibliotecas. Depois executar:

```
dotnet run --project Generator/Generator.csproj -p:AltiumSharpRoot=/caminho/AltiumSharp -- /caminho/pasta-descompactada
```

O gerador lê pinagem.csv e o STEP externo e grava/revalida o par na subpasta Nativo_Altium. Reflexão é usada apenas para acessar métodos internos de autoria de implementação e mapeamento nessa versão fixada da API. Não há executável necessário para usar as bibliotecas no Altium.
