# Instalador gráfico — Reversível e Protegido com atualizações

Destinado exclusivamente à DevKit **ESP32-S3 N16R8** e carrier CNC_FFST S3 R2. Não usar na DLC32 V2.1 com ESP32 clássico, nem na DLC32 MAX. Não houve ensaio físico deste provisionamento ou das atualizações. Validar em um módulo de avaliação antes de proteger placas destinadas a clientes.

## Abrir no Windows

1. Instalar Python 3.12 com Tkinter (incluído no instalador oficial).
2. Extrair completamente o ZIP `CNC_FFST_S3_Instalador_0.2.0.zip` em uma pasta local com permissão de escrita. Manter a pasta `CNC_FFST_S3` de fontes.
3. Abrir `Instalador_CNC_FFST_S3.py`, ou executar `py -3.12 Instalador_CNC_FFST_S3.py` no PowerShell da pasta extraída.
4. Clicar em **Instalar dependências**. Requer internet: esptool 4.8.1, bitstring 4.3.1 e pyserial 3.5.
5. Usar a **USB/serial da DevKit**, fechar outros programas que usam a porta e deixar motores, laser e spindle fisicamente sem alimentação.

O instalador é um único arquivo Python. Para compilar o perfil protegido ele utiliza a pasta de fontes fornecida. Não há EXE Windows compilado/testado nesta entrega. O aplicativo de controle CNC continua separado do instalador; o Python de controle deve corresponder ao BIN gravado.

## Programa Fabricação Fresa Laser

O programa de controle estava identificado como `CNC_FFST_Unico.py`. O pacote agora traz o mesmo programa em arquivo único com o nome **Fabricação Fresa Laser.py**, separado do instalador.

- Executar `INSTALAR_DEPENDENCIAS_CONTROLE.cmd` uma vez para instalar pyserial/Pillow.
- Executar `ABRIR_FABRICACAO_FRESA_LASER.cmd` para abrir o controle.
- Fechar o instalador antes de conectar no controle. Selecionar/digitar a porta, por exemplo COM8, e usar 115200 baud.
- O programa da raiz é para o BIN **UART reversível 0.1.0** fornecido. A placa sem o condicionamento da carrier pode indicar limites/emergência ativos; não desativar essas proteções para movimentar.
- Para o perfil protegido, preparar o firmware com sua chave e usar `python/PROTECTED/Fabricação Fresa Laser.py` gerado na mesma preparação. Sua credencial e identificação estarão embutidas; o BIN protegido completo não estará no programa de controle.

## Opção Reversível

Selecionar **Reversível** (opção inicial). Selecionar a porta e o BIN UART completo fornecido; clicar em **GRAVAR E VERIFICAR**.

O instalador valida tamanho de 16 MB, chip das imagens, checksum, SHA256, tabela de partições e hash de uma imagem reconhecida. Identifica ESP32-S3 e flash de 16 MB antes de escrever em 0x0. Não comprova PSRAM, pinagem, segurança elétrica ou funcionamento da CNC.

Não grava eFuses neste modo. É possível regravar outros firmwares por ferramentas compatíveis, desde que a placa não tenha sido protegida anteriormente. Este modo não impede a extração/clonagem do firmware. A autenticação do programa CNC permanece ativa.

O instalador aceita as imagens fornecidas e as protegidas preparadas localmente; não é um gravador genérico para qualquer BIN de qualquer placa. A placa em modo reversível continua livre para usar outras ferramentas de gravação.

## Opção Protegido com atualizações

Este modo usa:

- Flash Encryption **AES-XTS-256 em Release**: uma chave de 64 bytes diferente por placa (dois blocos de eFuse de 256 bits).
- Secure Boot V2 RSA-3072: uma chave privada de assinatura para seu projeto; a placa confia no resumo da chave pública.
- Chaves AES protegidas contra leitura/escrita e bloqueio de JTAG.
- **Secure ROM Download**, preservado para atualizar com bytes previamente criptografados no computador. O instalador não desabilita completamente o modo de download.
- Autenticação HMAC atual, mantida e independente das chaves acima.

A leitura física da flash pode obter ciphertext. Esse conteúdo não constitui um BIN utilizável em outra ESP32, que terá outra chave. Não é uma garantia absoluta contra toda forma de ataque físico ou vulnerabilidade de software.

**As proteções não são reversíveis.** Atualizar é permitido; voltar à condição de um ESP32-S3 sem proteções ou instalar qualquer BIN comum não é. As alterações de eFuses começam na gravação das chaves pelo instalador, antes do primeiro boot do BIN protegido. O primeiro boot conclui criptografia, Secure Boot e restrições.

### Preparar seu firmware e sua assinatura

1. Testar hardware, movimento, limites, emergência e sonda com o perfil reversível, sem proteção permanente. A compilação não valida esses testes.
2. Selecionar **Pasta de chaves** em local privado e **Pasta de backup** em outro local, preferencialmente outro dispositivo. Pastas sobrepostas são recusadas.
3. Clicar em **Preparar firmware protegido** e selecionar a pasta `CNC_FFST_S3` extraída.
4. A interface gera `secure_boot_signing_key.pem` na pasta de chaves e copia para backup. Ela instala PlatformIO 6.1.18 e compila o ambiente `cnc_ffst_s3_n16r8_protected`. A primeira preparação pode baixar vários GB e levar minutos.
5. O empacotamento assina bootloader e aplicação e verifica as assinaturas. O BIN completo gerado fica em `CNC_FFST_S3/artifacts/PROTECTED/`; o instalador o seleciona automaticamente e registra seu hash em `imagens_locais.json` ao lado do instalador.
6. O Python de controle protegido embute somente o registro da credencial HMAC e a identidade esperada, não o BIN completo, a chave AES ou a assinatura privada. Distribuir apenas esse arquivo/EXE de controle aos clientes. Ele fica em `CNC_FFST_S3/python/PROTECTED/CNC_FFST_Unico.py`. Use esse arquivo com o BIN protegido recém-compilado.

A chave privada do computador usado para testar este repositório não é distribuída. O instalador exige que a chave privada local corresponda ao BIN para o provisionamento. Assim você mantém a capacidade de assinar futuras versões com sua própria chave. Não exclua ou troque essa chave ao recompilar.

A preparação não grava nada na placa. O BIN protegido em disco ainda é plaintext assinado: não distribuí-lo nem fornecer arquivos de chave ao cliente. O objetivo é entregar somente a placa já provisionada.

### Provisionar cada placa

1. Selecionar a porta USB/serial e o BIN preparado; selecionar **Protegido com atualizações** e a confirmação de modelo/cargas desligadas.
2. Selecionar novamente as mesmas pastas de chaves e backup.
3. Clicar em **GRAVAR E VERIFICAR** e digitar `PROTEGER` na confirmação específica.
4. O programa consulta os eFuses públicos. Recusa provisionamento quando detectar proteções/finalidades de chaves já configuradas; não tenta sobrescrevê-las.
5. Gera a chave exclusiva da placa, salva em ambas as pastas por MAC e confere o backup antes de qualquer `burn_key`. Grava as duas metades nos blocos KEY0/KEY1 com as finalidades AES256 adequadas, protegendo leitura/escrita por padrão do espefuse.
6. Grava o BIN completo mantendo o chip em download ROM e verifica antes de sair. A janela não permite fechar durante a operação.
7. Quando indicado, apertar RESET uma vez e manter alimentação estável. Aguardar pelo menos 60 segundos, sem interromper a criptografia inicial. Esse tempo é uma margem operacional, não confirmação de sucesso.
8. Clicar em **Conferir proteção**. O firmware responde a um nonce novo com relatório HMAC contendo MAC, hash da aplicação e estados de Release, Secure Boot, download seguro, JTAG e proteção das chaves. Só então a interface informa proteção reportada pelo firmware autenticado. Salvar o registro.

Em caso de erro após gravar qualquer eFuse, não repetir o provisionamento, apagar os registros ou gerar outra chave para o MAC. Guardar logs, estado e chaves para diagnóstico. A consulta após boot não substitui ensaio físico independente de clonagem.

## Atualizar uma placa protegida

1. Manter a chave de assinatura original e as chaves AES por placa. Não alterar layout de partições nesta modalidade de atualização.
2. Incorporar suas mudanças no código e clicar em **Preparar firmware protegido** usando as mesmas pastas. O processo reutiliza a assinatura e registra a nova imagem. Não clicar em gravar/provisionar novamente uma placa já protegida.
3. Fechar o programa CNC; desconectar energia de motores/ferramentas. Selecionar o BIN novo, porta e pasta de chaves.
4. Clicar em **Atualizar placa protegida**.
5. O instalador autentica o relatório do firmware em execução, identifica o MAC, carrega a chave local correspondente, valida hashes/registros e criptografa **somente a aplicação assinada**, no endereço 0x30000.
6. Confere Secure Boot e criptografia pela ROM segura e grava o ciphertext nesse endereço. Não regrava bootloader, tabela de partições, configurações ou eFuses.
7. Depois do reset confere pelo firmware autenticado o hash novo e os estados de segurança. Um erro ou ausência de resposta deixa a atualização sem confirmação.

O uso interno de `--force` fica restrito a esta escrita de aplicação **já criptografada no computador**, necessária porque o esptool não distingue esse ciphertext de um BIN plaintext. O instalador normal/provisionamento não usa essa opção, nem `--encrypt` na ROM em modo Release. Não reproduzir esse comando manualmente com BIN plaintext.

A atualização por USB sobrescreve a aplicação única; **não há OTA Wi-Fi, partição de rollback ou atualização tolerante a corte de energia**. Se houver interrupção/corrupção e o aplicativo deixar de responder, o fluxo automático recusa continuar sem autenticação. Recuperação assistida com a chave correta, endereço e identidade física pode ser necessária. Não há recuperação automática implementada nesta entrega.

## Arquivos a preservar

Na pasta de chaves e no backup:

```text
secure_boot_signing_key.pem       # privada do projeto: assina futuras versões
<MAC>/flash_key.bin               # 64 bytes, exclusiva daquela placa
<MAC>/key_part1.bin
<MAC>/key_part2.bin
<MAC>/device.json                 # identificação, hashes e fase do processo
```

Os registros do backup começam na fase `prepared`; o arquivo principal registra as fases seguintes. As chaves são iguais nos dois locais e não mudam nas atualizações. Os arquivos são privados e não criptografados por este programa; proteger o acesso e o armazenamento, inclusive ACLs no Windows. Não publicar pastas de chaves, backups ou os PEMs privados no GitHub. A assinatura pública não é segredo.

Perder a chave AES impede este método de atualização daquela placa. Perder a assinatura privada impede assinar novas versões aceitas por todas as placas que confiam nela. Perder ambas não impede que o firmware já instalado continue funcionando, mas limita manutenção.

A autenticação HMAC usa a credencial comum já autorizada no projeto; ela não substitui as duas classes de chave acima. Conhecer apenas o MAC não permite derivar a chave AES aleatória.

## Validação e limites desta entrega

Compilação real ESP32-S3, assinaturas RSA verificadas com espsecure, criptografia AES-XTS com ida/volta e chave errada rejeitada por comparação, eFuses **virtuais** com finalidades/proteções verificadas e testes de fluxo do instalador. Interface Tk aberta em ambiente Linux; gravação, bloqueios e atualização orquestrados com transporte simulado.

Não houve conexão com placa real, gravação física, ativação física de eFuses, teste Windows, falha de energia, recuperação, extração/clonagem ou validação dos tempos elétricos da CNC. A base ESP-IDF 4.4.3 foi mantida para compatibilidade com o driver; esta entrega exige revisão e ensaio antes de uso em produção. O provisionamento deve ser tratado como experimental até esses ensaios.
