# CNC_FFST — guia local de compilação

DLC32 V2.1, sem display, com seleção manual entre laser e spindle.
Este guia NÃO serve para a DLC32 MAX (ESP32-S3).

Há duas fontes independentes:

| Versão | Autenticação | Quem pode executar movimentos |
| --- | --- | --- |
| 0.2.0 | Não | Senders GRBL comuns |
| 0.3.0 | Sim, chave compartilhada | Cliente com assinatura HMAC válida |

A versão 0.3.0 mantém consultas e calibrações GRBL permitidas acessíveis sem
assinatura. Movimentos, homing, jog, sondagem e ferramentas exigem autenticação.
A chave pode ser extraída do BIN/EXE/Python; não é proteção contra engenharia reversa.

## 1. Instalar os programas no Windows

1. Instale Python 3.12 de https://www.python.org/downloads/ . Marque a opção
   “Add python.exe to PATH”. Feche e abra o terminal após instalar.
2. Instale VS Code de https://code.visualstudio.com/ .
3. A extensão PlatformIO IDE é opcional para os comandos deste guia, mas facilita
   abrir/editar o projeto. Instale-a pelo painel Extensions do VS Code se desejar.
4. Tenha Internet para baixar pacotes Python, PlatformIO e ferramentas ESP32.
5. Para COMPILAR, a placa não precisa estar conectada e o driver USB não é necessário.
   Para GRAVAR depois, a porta USB e o driver adequado da placa precisam funcionar.

Use o terminal PowerShell do VS Code ou do Windows. Os comandos abaixo não
precisam de privilégios de administrador nem de executar Activate.ps1.

Confira o Python:

```powershell
py -3.12 --version
```

Se esse comando não existir, confira a instalação/launcher do Python. Não
substitua por outro Python sem conferir que ele é a versão 3.12.

## 2. Baixar e organizar as duas cópias

Sem autenticação:
https://github.com/fabiooferreira/MKS_DLC32/archive/refs/heads/cnc-ffst-v0.2.0-test.zip

Com autenticação:
https://github.com/fabiooferreira/MKS_DLC32/archive/refs/heads/cnc-ffst-v0.3.0-auth.zip

O “test” no nome da branch 0.2.0 é histórico. A identificação do firmware foi
alterada para CNC_FFST 0.2.0, sem esse sufixo.

Extraia cada ZIP em local separado. Dentro de cada extração existe uma pasta
chamada CNC_FFST. Copie/renomeie ESSA pasta para obter a estrutura abaixo:

```text
C:\CNC_FFST\sem_autenticacao\Firmware\platformio.ini
C:\CNC_FFST\sem_autenticacao\tools\build.sh
C:\CNC_FFST\sem_autenticacao\artifacts\...

C:\CNC_FFST\com_autenticacao\Firmware\platformio.ini
C:\CNC_FFST\com_autenticacao\tools\prepare_shared_key.py
C:\CNC_FFST\com_autenticacao\python\...
C:\CNC_FFST\com_autenticacao\artifacts\CNC_FFST_0.3.0_FULL_4MB.bin
```

Não coloque a versão 0.3.0 sobre a 0.2.0. Não misture bibliotecas, headers,
partições, caches ou artefatos das duas cópias. O ZIP já traz as fontes extraídas:
não é necessário extrair novamente o antigo MKS-DLC32-FIRMWARE-main.zip.

Arquivos BIN já presentes nos ZIPs são resultados anteriores. Só considere um
arquivo como uma nova compilação depois de o build atual terminar com SUCCESS.

## 3. Preparar as ferramentas — repetir em cada pasta

Primeiro abra a pasta SEM autenticação:

```powershell
Set-Location C:\CNC_FFST\sem_autenticacao
py -3.12 -m venv .venv-build
if ($LASTEXITCODE -ne 0) { throw 'Falha ao criar o ambiente Python' }
.\.venv-build\Scripts\python.exe -m pip install -r tools\requirements-build.txt esptool==4.8.1
if ($LASTEXITCODE -ne 0) { throw 'Falha ao instalar as ferramentas' }
$env:PLATFORMIO_CORE_DIR = Join-Path $PWD '.platformio-core'
.\.venv-build\Scripts\python.exe -m platformio --version
```

A versão do PlatformIO deve ser 6.1.18. A plataforma ESP32 é fixada pelo projeto
em espressif32 3.2.0, com Arduino ESP32 1.0.6. Não atualize automaticamente para a
plataforma mais nova durante este procedimento.

Faça a mesma preparação na pasta COM autenticação:

```powershell
Set-Location C:\CNC_FFST\com_autenticacao
py -3.12 -m venv .venv-build
if ($LASTEXITCODE -ne 0) { throw 'Falha ao criar o ambiente Python' }
.\.venv-build\Scripts\python.exe -m pip install -r tools\requirements-build.txt esptool==4.8.1
if ($LASTEXITCODE -ne 0) { throw 'Falha ao instalar as ferramentas' }
$env:PLATFORMIO_CORE_DIR = Join-Path $PWD '.platformio-core'
.\.venv-build\Scripts\python.exe -m platformio --version
```

A variável PLATFORMIO_CORE_DIR vale apenas para esse terminal. Por isso ela é
redefinida nos passos seguintes. Esses caches separados evitam confundir cópias.

## 4. Compilar SEM autenticação — 0.2.0

Execute este bloco no PowerShell:

```powershell
Set-Location C:\CNC_FFST\sem_autenticacao
$env:PLATFORMIO_CORE_DIR = Join-Path $PWD '.platformio-core'
.\.venv-build\Scripts\python.exe -m platformio run -d Firmware -e cnc_ffst_v2_1 -j 2
if ($LASTEXITCODE -ne 0) { throw 'Compilacao falhou: nao continue nem use o BIN antigo como resultado novo' }
New-Item -ItemType Directory -Force artifacts | Out-Null
Copy-Item Firmware\.pio\build\cnc_ffst_v2_1\firmware.bin artifacts\firmware.bin -Force
Copy-Item Firmware\.pio\build\cnc_ffst_v2_1\firmware.elf artifacts\firmware.elf -Force
```

Espere o download inicial das ferramentas e a mensagem SUCCESS. O alvo correto
é cnc_ffst_v2_1, mesmo na cópia sem autenticação.

O arquivo Firmware\.pio\build\cnc_ffst_v2_1\firmware.bin é SOMENTE a aplicação.
Ele ainda não é o arquivo único completo para gravação desde 0x0.

### Gerar o BIN único completo 0.2.0

Continue no mesmo terminal/pasta. Copie o bloco inteiro; o acento grave no fim
das linhas é a continuação de linha do PowerShell e não pode ter espaços depois.

```powershell
$fw = Join-Path $env:PLATFORMIO_CORE_DIR 'packages\framework-arduinoespressif32'
.\.venv-build\Scripts\python.exe -m esptool --chip esp32 merge_bin `
  --output artifacts\CNC_FFST_0.2.0_FULL_4MB.bin `
  --flash_mode dout --flash_freq 80m --flash_size 4MB --fill-flash-size 4MB `
  0x1000 "$fw\tools\sdk\bin\bootloader_dout_80m.bin" `
  0x8000 Firmware\.pio\build\cnc_ffst_v2_1\partitions.bin `
  0xe000 "$fw\tools\partitions\boot_app0.bin" `
  0x10000 artifacts\firmware.bin
if ($LASTEXITCODE -ne 0) { throw 'Falha ao gerar a imagem completa' }
Get-Item artifacts\CNC_FFST_0.2.0_FULL_4MB.bin | Select-Object Name, Length
Get-FileHash artifacts\CNC_FFST_0.2.0_FULL_4MB.bin -Algorithm SHA256
```

Resultado esperado: CNC_FFST_0.2.0_FULL_4MB.bin com 4.194.304 bytes.
Não há preparação de chave nem regeneração do cliente autenticado nesta versão.
Use um sender sem autenticação; o Python autenticado 0.3.0 recusa esse firmware.

## 5. Compilar COM autenticação — 0.3.0

### Preservar a chave compartilhada

Mantenha o BIN distribuído em:

```text
artifacts\CNC_FFST_0.3.0_FULL_4MB.bin
```

Antes de compilar pela primeira vez, o script recupera a mesma chave desse BIN.
Depois, guarda uma cópia em .private\shared_key.bin e gera o header local
Firmware\Grbl_Esp32\src\FFSTSharedKey.generated.h.

Se não houver nem a cópia .private nem um BIN com a chave, o script gera uma
NOVA chave. Essa nova família não será compatível com os clientes/placas antigos.
Não apague a pasta .private para “limpar” a compilação. Guarde backup privado da
chave e guarde o conjunto BIN/Python correspondente. O header não vem no Git
porque é gerado localmente; sua ausência antes desse passo é normal.

Execute:

```powershell
Set-Location C:\CNC_FFST\com_autenticacao
$env:PLATFORMIO_CORE_DIR = Join-Path $PWD '.platformio-core'
if (!(Test-Path .private\shared_key.bin) -and !(Test-Path artifacts\CNC_FFST_0.3.0_FULL_4MB.bin)) { throw 'Pare: faltam a chave preservada e o BIN original para recupera-la' }
.\.venv-build\Scripts\python.exe tools\prepare_shared_key.py
if ($LASTEXITCODE -ne 0) { throw 'Falha ao preparar a chave' }
.\.venv-build\Scripts\python.exe -m platformio run -d Firmware -e cnc_ffst_v2_1 -j 2
if ($LASTEXITCODE -ne 0) { throw 'Compilacao falhou: nao continue nem use o BIN antigo como resultado novo' }
New-Item -ItemType Directory -Force artifacts | Out-Null
Copy-Item Firmware\.pio\build\cnc_ffst_v2_1\firmware.bin artifacts\firmware.bin -Force
Copy-Item Firmware\.pio\build\cnc_ffst_v2_1\firmware.elf artifacts\firmware.elf -Force
```

Só continue depois de SUCCESS. Não remova CNC_FFST_AUTH para tentar resolver
um erro de build: isso altera a política de proteção do firmware.

### Gerar o BIN único completo 0.3.0

```powershell
$fw = Join-Path $env:PLATFORMIO_CORE_DIR 'packages\framework-arduinoespressif32'
.\.venv-build\Scripts\python.exe -m esptool --chip esp32 merge_bin `
  --output artifacts\CNC_FFST_0.3.0_FULL_4MB.bin `
  --flash_mode dout --flash_freq 80m --flash_size 4MB --fill-flash-size 4MB `
  0x1000 "$fw\tools\sdk\bin\bootloader_dout_80m.bin" `
  0x8000 Firmware\.pio\build\cnc_ffst_v2_1\partitions.bin `
  0xe000 "$fw\tools\partitions\boot_app0.bin" `
  0x10000 artifacts\firmware.bin
if ($LASTEXITCODE -ne 0) { throw 'Falha ao gerar a imagem completa' }
Get-Item artifacts\CNC_FFST_0.3.0_FULL_4MB.bin | Select-Object Name, Length
Get-FileHash artifacts\CNC_FFST_0.3.0_FULL_4MB.bin -Algorithm SHA256
```

Resultado esperado: CNC_FFST_0.3.0_FULL_4MB.bin com 4.194.304 bytes.

### Atualizar o Python para corresponder ao BIN novo

Este passo é obrigatório na versão autenticada, mesmo preservando a chave:
o programa também confere o hash exato da aplicação. Uma nova compilação pode
mudar esse hash mesmo com o mesmo número de versão.

```powershell
.\.venv-build\Scripts\python.exe tools\write_firmware_identity.py
if ($LASTEXITCODE -ne 0) { throw 'Falha ao validar a imagem/gerar a identidade' }
.\.venv-build\Scripts\python.exe tools\bundle_python.py
if ($LASTEXITCODE -ne 0) { throw 'Falha ao gerar o Python unico' }
.\.venv-build\Scripts\python.exe -m py_compile python\CNC_FFST_Unico.py
if ($LASTEXITCODE -ne 0) { throw 'Falha de sintaxe no Python gerado' }
```

Esses comandos validam o checksum/digest da aplicação, geram o manifesto,
copiam o BIN novo para os recursos do cliente e geram python\CNC_FFST_Unico.py
com os dados embutidos. Use ESSE Python junto de ESSE BIN.

Para executar no mesmo ambiente:

```powershell
.\.venv-build\Scripts\python.exe -m pip install -r python\requirements.txt
if ($LASTEXITCODE -ne 0) { throw 'Falha ao instalar dependencias do programa' }
.\.venv-build\Scripts\python.exe python\CNC_FFST_Unico.py
```

Não é necessário parear nem colocar uma chave externa ao lado desse Python.
Se usar o Montador de Páginas, substitua a página antiga pelo novo
CNC_FFST_Unico.py, selecione a entrada App e gere novamente o programa montado.
Um programa/EXE já montado não incorpora mudanças sozinho.

### Gerar o EXE Windows, se desejar

Depois de atualizar o Python único:

```powershell
.\.venv-build\Scripts\python.exe -m pip install pyinstaller==6.16.0
if ($LASTEXITCODE -ne 0) { throw 'Falha ao instalar PyInstaller' }
.\.venv-build\Scripts\python.exe -m PyInstaller --noconfirm --clean --onefile --windowed --name CNC_FFST_Controlador python\CNC_FFST_Unico.py
if ($LASTEXITCODE -ne 0) { throw 'Falha ao gerar o executavel' }
```

O resultado fica em dist\CNC_FFST_Controlador.exe. Não precisa de --add-data
para os recursos de autenticação do arquivo único. Ícones externos personalizados
pelo usuário, se usados, continuam sendo recursos separados do programa original.
O EXE de um programa montado com outras páginas deve ser reconstruído a partir
DO arquivo gerado pelo Montador, com as dependências de todas as páginas.

## 6. Qual BIN usar e em qual endereço

| Arquivo | Tipo | Base de gravação |
| --- | --- | --- |
| firmware.bin | Só aplicação | 0x10000 |
| CNC_FFST_0.2.0_FULL_4MB.bin | Imagem única completa, sem autenticação | 0x0 |
| CNC_FFST_0.3.0_FULL_4MB.bin | Imagem única completa, com autenticação | 0x0 |

Para o fluxo de um único BIN, escolha o arquivo que contém FULL_4MB no nome.
Não grave firmware.bin em 0x0. Não misture bootloader/partições de outra placa.
No MKSLaserTool, use somente o procedimento de imagem completa desde 0x0;
confira as opções da versão da ferramenta. Em dúvida, use uma ferramenta que
permita informar o endereço explicitamente em vez de adivinhar.

A imagem completa inclui áreas vazias de NVS/SPIFFS. Gravá-la sobrescreve
calibrações, configurações Wi-Fi e arquivos existentes. Antes de gravar, faça
backup da flash/configurações. Mantenha laser e spindle sem alimentação.
Depois, restaure e confira calibração, limites, homing, sonda e seleção de modo
antes de permitir movimento. O ALARM inicial continua intencional nas duas versões.
Compilar ou gerar um EXE não comprova segurança física nem precisão de sondagem.

## 7. Configurar laser e spindle depois

As duas versões são da DLC32 V2.1 e mantêm o GPIO32 original. A chave física
não é detectada pelo firmware. Troque ferramenta com trabalho parado e ferramentas
sem energia, e confira modo/driver correspondentes:

- Laser: Spindle/Type=LASER, $32=1.
- Spindle: Spindle/Type=PWM, $32=0.

Os comandos de configuração são $Spindle/Type=LASER ou $Spindle/Type=PWM.
Na versão autenticada, use a caixa de comandos do Python autenticado para
configurações protegidas. Calibre a escala S e o controlador do spindle conforme
a máquina: a base MKS tem uma implementação PWM com escala fixa por 1000.
Não presuma que apenas mudar $30 calibra RPM reais. Veja docs/LASER_SPINDLE.md.

## 8. Solução de problemas

- “FFSTSharedKey.generated.h: No such file”: execute prepare_shared_key.py na
  raiz correta da versão 0.3.0 antes de compilar.
- PlatformIO tenta usar outra instalação: confira $env:PLATFORMIO_CORE_DIR e use
  o python.exe da .venv-build mostrado neste guia.
- Erro de download/TLS: confira Internet/proxy/certificados. Não desative TLS,
  assinaturas ou checksums para contornar o problema.
- “No module named esptool/serial”: instale o pacote no MESMO python.exe que está
  executando o comando; não use um pip global de outra instalação.
- Build FAILED: procure o primeiro “error:” e pare. Não trate um BIN antigo já
  presente no repositório como resultado dessa compilação.
- Apenas “warning:”: não é necessariamente falha de build. Confira o resultado
  final SUCCESS e registre os avisos. As fontes herdadas têm avisos conhecidos.
- Python recusa versão/hash: refaça write_firmware_identity.py, bundle_python.py
  e o EXE/Montador após o BIN novo; confira que o BIN correspondente foi gravado.
- error:110 em movimento por outro sender na 0.3.0: bloqueio de autenticação
  esperado. Use o Python correspondente. Consultas/calibrações permitidas continuam.
- ALARM ao iniciar: não é erro de compilação nem autenticação. Só reconheça/homing
  após verificar a máquina; não automatize $X para ignorar a causa de um alarme.
- Porta COM ocupada: feche outros monitores/programas que usam a mesma USB.
- Reinícios: capture o log a 115200 baud e confira o arquivo/endereço gravado.
  Não apague a flash repetidamente como diagnóstico.

## 9. Alternativa Linux/macOS

Os scripts Bash do projeto são a alternativa já usada na nuvem. Dentro da raiz
da cópia escolhida, com Python 3.12/venv e Bash disponíveis:

```bash
export CNC_FFST_TOOLS_DIR="$PWD/.build-tools"
export PLATFORMIO_CORE_DIR="$PWD/.platformio-core"
bash tools/build-full.sh
```

Defina os dois caminhos em CADA cópia para não compartilhar estado por engano.
Na 0.3.0, preserve primeiro a chave/BIN existente conforme o passo 5.
O script compila, gera o BIN único e, na 0.3.0 atualizada, regenera o Python único.
Não execute os scripts Bash antigos diretamente no PowerShell sem Bash/Python3
compatíveis; use os comandos Windows deste guia.

## 10. O que foi verificado

As fontes 0.2.0 e 0.3.0 foram compiladas na nuvem Linux. A montagem dos BINs
completos, checksums/digests e autenticação em computador foram verificados.
O usuário confirmou conexão da placa V2.1 com o cliente corrigido. Isso não
valida todos os movimentos, sondagem e proteções físicas.

Os comandos PowerShell e a geração do EXE Windows são instruções baseadas nas
mesmas ferramentas/argumentos, mas não foram executados em um Windows nesta sessão.
Mantenha juntas as fontes, o BIN, o Python/EXE gerado e seus hashes para saber
exatamente qual conjunto está instalado. A DLC32 MAX permanece fora deste guia.

## 11. Extrair um BIN de backup da ESP32 pela USB

É possível ler a flash quando a placa permite acesso ao bootloader de download.
Desligue a alimentação do laser/spindle e feche outros programas que usam a COM.
A conexão do esptool pode reiniciar a controladora; não faça isso durante trabalho.
Use a porta real da sua placa no lugar de COM3. Para a DLC32 V2.1, o chip é esp32:

```powershell
.\.venv-build\Scripts\python.exe -m esptool --chip esp32 --port COM3 flash_id
.\.venv-build\Scripts\python.exe -m esptool --chip esp32 --port COM3 --baud 115200 read_flash 0x0 ALL backup_dlc32.bin
if ($LASTEXITCODE -ne 0) { throw 'Leitura falhou: nao considere o backup concluido' }
Get-Item backup_dlc32.bin | Select-Object Name, Length
Get-FileHash backup_dlc32.bin -Algorithm SHA256
```

ALL lê até o fim da flash detectada: uma placa com 8 MB gera backup de 8 MB,
mesmo que o firmware completo distribuído tenha 4 MB. Não reduza o tamanho do
backup para fazê-lo coincidir com o arquivo de distribuição.

Sem um ambiente Python já preparado, instale esptool==4.8.1 em um venv e execute
os mesmos argumentos com o python.exe desse ambiente. Não é necessário compilar
o firmware nem passar pela autenticação GRBL para ler pelo bootloader da ESP32.

A leitura é um dump da flash, não recuperação do código-fonte. Pode incluir
Wi-Fi, calibração, chave de autenticação e outros dados: guarde o backup privado,
fora das pastas que você publica no GitHub. Nesta edição CNC_FFST a autenticação
não ativa Secure Boot/Flash Encryption nem bloqueia a leitura pelo bootloader.
Se houver Flash Encryption ou restrições de download configuradas por eFuses,
a leitura pode ser bloqueada ou retornar dados cifrados, sem um BIN reutilizável.
Não altere eFuses para tentar contornar isso.

Este procedimento não foi executado na sua placa nesta sessão. Em caso de falha
de conexão, confira porta, cabo, alimentação e modo BOOT pelo procedimento da placa.
Não use erase_flash como tentativa de obter um backup.
