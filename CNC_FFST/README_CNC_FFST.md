# CNC_FFST 0.2.0

Firmware experimental para MKS DLC32 V2.1/ESP32, cartesiana XYZ, sem display.
Base: arquivo `MKS-DLC32-FIRMWARE-main.zip` do repositório
`fabiooferreira/MKS_DLC32`, commit `7aebcb3aa752424109a7d61eb93e5ade42aef4c4`.
GRBL-ESP32 declara GRBL 1.1, build 2022042101. A versão de produto original
é V2.1(8M.H35.20220421). Não foi inferido um commit upstream a partir dessa data.

## Estado

Versão para testes controlados. Compilação não valida comportamento físico,
detecção FIRE, precisão de sondagem, limites ou parada de emergência.
Não há sensor de chama instalado segundo o usuário. Esta base não contém
detecção FIRE/FLAME ativa; detalhes em [investigação](docs/FIRE_SONDAGEM.md).

## Imagem completa para gravação

Disponível `artifacts/CNC_FFST_0.2.0_FULL_4MB.bin`: conjunto de 4 MB para
base 0x0, com bootloader, partições e aplicação. Não confundir com firmware.bin
(aplicação em 0x10000). Leia [gravação completa](docs/GRAVACAO_COMPLETA.md)
antes de usar: esta imagem sobrescreve NVS e SPIFFS, incluindo calibração e Wi-Fi.
O empacotamento foi verificado; funcionamento em hardware permanece pendente.

## Compilar

Abra `Firmware` no VS Code com PlatformIO e selecione `cnc_ffst_v2_1`.
PlatformIO Core 6.1.18; plataforma Espressif32 3.2.0; TMCStepper 0.7.3.
O perfil original continua disponível para comparação.
O novo perfil seleciona o driver LASER e `$32=1` por padrão. Valores já salvos
na placa prevalecem: veja [configuração laser/spindle](docs/LASER_SPINDLE.md).

Na nuvem, com Python 3.12 e venv disponíveis:

```sh
bash /workspace/CNC_FFST/tools/build.sh
```

Em Linux/macOS local, execute na raiz do projeto:

```sh
export CNC_FFST_TOOLS_DIR="$PWD/.buildtools"
bash tools/build.sh
```

No Windows, use o terminal PlatformIO do VS Code, dentro de `Firmware`:

```text
pio run -e cnc_ffst_v2_1 -j 2
```

Saída: `Firmware/.pio/build/cnc_ffst_v2_1/firmware.bin`.
O script também copia BIN/ELF, log, hashes e lista de pacotes para `artifacts`.
O arquivo BIN é imagem de aplicação: não é uma imagem mesclada de toda a flash.
Para gravação inicial, use `pio run -e cnc_ffst_v2_1 -t upload --upload-port PORTA`
após conferir placa, alimentação e procedimento de segurança. O perfil herda
`COM8` da base; passe a porta real explicitamente. Não grave no offset zero.
Offsets e arquivos auxiliares devem ser os produzidos pelo PlatformIO para este alvo.
Não foi realizada gravação em hardware durante este trabalho.

Dependências de rede: PyPI, registro/downloads PlatformIO e espelhos retornados
pelo registro. Verificação TLS/checksums permanece habilitada.
O lock de ferramentas Python está em `tools/requirements-build.txt`; versões
resolvidas do firmware estão em `artifacts/packages.txt` após a compilação.
As bibliotecas originais vendorizadas foram preservadas.

## Operação e limitações

Serial: 115200 baud. O banner permanece `Grbl 1.1` para compatibilidade e adiciona
uma mensagem CNC_FFST; `$I` inclui `CNC_FFST-0.2.0` no campo de build.
O Wi-Fi mantém a implementação e configurações NVS da base e inicializa sem LCD.
Não há troca automática entre ferramentas: laser e spindle compartilham PWM GPIO32.
Seleção física, intertravamento e configuração de modo são responsabilidade da máquina.
O firmware não implementa compensação de malha: o sender precisa gerar/aplicar o
mapeamento PCB usando os resultados `[PRB:...]` de G38.x.

Ao ligar, o perfil entra em ALARM. Confira máquina e sensores antes de `$H` ou `$X`.
Não apague NVS nem execute `$RST=*` sem backup de `$$`, `$+`, `$N`, `$#` e parâmetros Wi-Fi.
Os defaults originais deixam limites e homing desabilitados; habilite e calibre
conforme os sensores reais. `$22` não deve ser habilitado sem verificar os ciclos
de homing: a base faz X/Y, não Z. Veja [plano de testes](docs/TESTES_HARDWARE.md).

Não existe pino dedicado de E-stop configurado nesta base. O reset serial Ctrl-X
e os caminhos de limites/safety door foram preservados, mas não substituem uma
parada física que corte a energia das ferramentas. Não foi inventada uma entrada
de emergência nem alterada a pinagem para contornar essa limitação.

Fontes GPL e LICENSE originais preservados. Veja [alterações](docs/ALTERACOES.md)
e o patch completo `docs/CNC_FFST.patch` para auditoria.
