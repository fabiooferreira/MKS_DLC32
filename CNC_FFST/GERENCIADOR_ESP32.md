# CNC_FFST — Gerenciador DLC32 V2.1, versão 2.0

Interface única em `python/Gerenciador_ESP32_DLC32.py` para consultar a placa, importar/analisar relatórios, preparar ferramentas, compilar o projeto local, criar backup e gravar/verificar o BIN completo por USB.

**A etapa de proteção está visível, mas bloqueada. As fontes atuais geram firmware normal, sem criptografia de flash. Este programa não grava eFuses.** Autenticação do aplicativo continua sendo a da versão 0.3.0 e não impede a leitura da flash. A ativação exigirá um bootloader compatível e um procedimento de provisionamento/atualização validado em hardware.

Somente MKS DLC32 V2.1, ESP32 clássico/WROOM-32U, flash de 4 MB, sem display. Não serve para DLC32 MAX/ESP32-S3. O modelo da PCB precisa ser confirmado fisicamente: ele não pode ser deduzido apenas do chip.

## Abrir no Windows

1. Instale Python **3.12**, incluindo Tkinter e o launcher `py`, pelo instalador oficial. Marque Add Python to PATH.
2. Extraia o ZIP do gerenciador.
3. Execute `Iniciar_Gerenciador.bat`, ou abra o terminal nessa pasta:

```powershell
py -3.12 Gerenciador_ESP32_DLC32.py
```

A interface em si usa a biblioteca padrão. Na aba **Ferramentas**, confira o Python e a pasta de trabalho e clique em **Preparar ferramentas**. Isso cria um ambiente isolado em `venv-ferramentas` e instala:

- PlatformIO 6.1.18;
- esptool 4.8.1;
- bitstring 4.3.1;
- pyserial 3.5.

Internet é necessária para preparar as ferramentas e para os downloads iniciais do PlatformIO. Não é necessário executar como administrador. A versão da plataforma ESP32 continua sendo `espressif32@3.2.0`, conforme as fontes existentes. No Linux, instale também os pacotes Python venv e Tkinter da distribuição.

A pasta de trabalho padrão é `CNC_FFST_Gerenciador` dentro da pasta pessoal. Quando usado no Montador de Páginas, fica dentro de `CNC_PCBS_CONFIG_DIR`. Você pode escolher outra pasta. Evite pastas públicas, temporárias ou dentro do repositório, especialmente para backups.

## 1. Consultar ou importar relatório

Pare o trabalho, desligue laser/spindle e feche outros controladores antes de consultar a porta. As ferramentas podem reiniciar a placa. Confirme as duas caixas abaixo das abas.

Na aba **Placa e relatório**:

1. Clique em Atualizar portas e selecione a USB.
2. Clique em Consultar placa por USB.
3. Confira a análise e salve o relatório JSON para enviar, se necessário.

Também é possível importar o JSON da versão anterior do gerenciador. O programa recalcula as conclusões e descarta campos extras; não aceita uma conclusão de segurança simplesmente porque veio no JSON.

O relatório contém MAC, chip/revisão, cristal, tamanho da flash e os campos públicos selecionados de eFuses. Não contém chaves, blocos de chave, senha Wi-Fi ou conteúdo da flash. O MAC é o identificador único usado no inventário; nesta versão não existe vínculo do firmware ao MAC.

Consultas concluídas também guardam uma cópia em `relatorios/<MAC>/<data UTC>.json` na pasta de trabalho.

Um relatório importado permite análise. **Ele não substitui a consulta atual da placa antes de backup/gravação.** A revisão é registrada para a análise técnica; esse relatório não certifica sozinho a compatibilidade de qualquer firmware ou a proteção completa contra extração.

## 2. Selecionar as fontes locais

Baixe e extraia o projeto completo correspondente. O ZIP do gerenciador contém a interface, não embute o código-fonte inteiro do firmware.

Com autenticação, versão 0.3.0:
https://github.com/fabiooferreira/MKS_DLC32/archive/refs/heads/cnc-ffst-v0.3.0-auth.zip

Sem autenticação, versão 0.2.0:
https://github.com/fabiooferreira/MKS_DLC32/archive/refs/heads/cnc-ffst-v0.2.0-test.zip

O nome histórico da branch 0.2.0 contém `test`; a identificação no firmware permanece CNC_FFST 0.2.0, sem esse sufixo. Não misture as duas cópias.

Na aba **Compilar**, selecione a pasta `CNC_FFST` que contém `Firmware/platformio.ini` e `tools/`. A raiz do repositório também é aceita, quando contém essa pasta. Clique em Conferir perfil do projeto.

O perfil é detectado pelas fontes, não pelo relatório:

| Fontes | Resultado |
| --- | --- |
| CNC_FFST 0.3.0 com flag de autenticação | Mantém autenticação e gera cliente Python correspondente |
| CNC_FFST 0.2.0 sem flag de autenticação | Gera firmware sem autenticação; não gera cliente autenticado |

A interface não retira autenticação nem altera pinagem para adaptar uma versão à outra. O projeto selecionado contém código e scripts que serão executados; use somente fontes confiáveis.

## 3. Compilar

Clique em **Compilar e gerar pacote completo**. A placa não precisa estar conectada. O fluxo usa o ambiente `cnc_ffst_v2_1`, paralelismo 2 e o cache PlatformIO da pasta de trabalho.

Na versão autenticada, o gerenciador exige a credencial existente em `.private/shared_key.bin` ou no BIN 0.3.0 incluído no projeto. Se não a encontrar, ou encontrar divergência entre as duas cópias, interrompe a compilação. Não cria uma nova chave silenciosamente.

Cada execução tem uma pasta própria em `compilacoes/<data UTC>/`, com:

- `CNC_FFST_0.x.0_FULL_4MB.bin`: imagem única, exatamente 4.194.304 bytes, base **0x0**;
- `pacote.json`: versão, perfil, endereço e hashes do BIN;
- `firmware_app_0x10000.bin`: aplicação separada, não usar em 0x0;
- `firmware.elf`, quando produzido;
- `compilacao.log`: saída completa, incluindo erros e avisos;
- na versão autenticada, `CNC_FFST_Unico.py` e `firmware_identity.json` correspondentes à aplicação compilada.

O gerenciador confere checksum/SHA256 internos, chip da imagem, tamanho, DOUT/80 MHz/4 MB, tabela `huge_app`, identificação interna e registro da credencial quando aplicável. O manifesto só é escrito depois da conclusão bem-sucedida. Se a compilação falhar, a seleção anterior de pacote é limpa. Saídas parciais não são pacotes válidos.

**Use o novo `CNC_FFST_Unico.py` com o novo BIN autenticado.** A autenticação atual verifica o hash exato da aplicação; o cliente antigo pode recusar uma recompilação. Se usar EXE, gere novamente o executável a partir do Python novo. O gerenciador não gera o EXE automaticamente.

Hashes detectam alteração acidental; `pacote.json` não é uma assinatura de procedência. Uma compilação concluída não valida movimento, sondagem ou segurança na máquina real.

## 4. Backup e gravação

Na aba **Gravar**, selecione o `pacote.json` da compilação desejada e clique em Conferir pacote. Não selecione um BIN de aplicação como imagem completa. Não há opção para gravar um BIN arbitrário sem o pacote e suas verificações.

Antes de gravar, o gerenciador:

1. Consulta novamente a placa por USB e compara identidade, tamanho da flash e eFuses com o relatório.
2. Bloqueia gravação convencional quando encontra estados de proteção alterados, incluindo contagem de criptografia não nula, flags de segurança ou campos travados. Mesmo contagem par cuja criptografia esteja inativa exige análise específica.
3. Cria backup completo de 4 MB, confere o tamanho e registra SHA256. Falha no backup interrompe a gravação.
4. Reconsulta a placa, grava a imagem completa em **0x0** e executa `verify_flash`.
5. Registra sucesso apenas se gravação e comparação terminarem sem erro.

A confirmação mostra MAC, porta, versão e presença/ausência de autenticação. **O BIN completo substitui calibrações GRBL, Wi-Fi, NVS e arquivos antigos.** Guarde os valores necessários e revise-os após gravar.

O backup fica em `backups/<MAC>/<data UTC>/flash.bin`, com `backup.json`. Ele contém dados privados e possivelmente credenciais: **não envie o backup para análise nem publique no GitHub**. Envie apenas o relatório JSON de diagnóstico. Em sistemas POSIX o arquivo de backup recebe permissão 0600; no Windows a proteção depende das permissões da pasta/conta. O botão de backup avulso usa as mesmas verificações.

Uma leitura incompleta fica como `.part`, sem metadados de backup concluído. A interface não oferece restauração automática de backups.

Cada gravação tem `gravacoes/<data UTC>/gravacao.json`, a imagem usada e `usb.log`. Falhas ficam registradas como falha, inclusive quando a escrita terminou mas a comparação falhou. Não desconecte ou troque a placa durante as operações.

Depois, confirme boot e conexão autenticada e faça testes controlados de limites, emergência, laser/spindle e sondagem. Sucesso na comparação da flash não é teste funcional nem valida a correção de FIRE/FLAME.

## 5. Proteção

A aba explica o bloqueio e não oferece operação de gravação de eFuses, nem por parâmetro de linha de comando. Não há uso de `--force` para contornar proteções. Placas com download UART bloqueado podem não permitir diagnóstico; o programa registra a falha, sem tentar desbloquear.

Para acrescentar a proteção posteriormente, faltam um bootloader/aplicação compatíveis, a seleção de configurações conforme a revisão e os eFuses reais, uma chave de criptografia por placa, política de atualização/recuperação e validação física. A chave de autenticação compartilhada do seu Python tem outra finalidade e não substitui a chave de criptografia.

Um firmware vinculado ao MAC seria uma alternativa para recusar execução em outra placa; **não impediria ler o BIN nem substituiria criptografia**. Essa alternativa não foi ativada nesta versão.

## Montador de Páginas

O arquivo expõe `App(parent)` e `create_page(parent)`, sem abrir outra janela ou executar `mainloop` quando importado. As ferramentas são chamadas pelo Python externo selecionado; não dependem de relançar o executável do Montador como se fosse um utilitário de gravação. Guarde a pasta de trabalho fora da extração temporária do Montador.

No uso independente, a janela pede que se aguarde a operação antes de fechar. No Montador, aguarde também antes de fechar a aplicação principal, pois ela controla o ciclo de vida das páginas.

## Validação e limites

Há testes em `tools/test_esp32_manager.py` para eFuse JSON real em modo virtual, campos de relatório, contagem de criptografia, bloqueios, pacotes reais 0.2.0/0.3.0, imagem corrompida, troca de placa, falha de backup, ordem backup/escrita/verificação e falha de comparação. A gravação nesses testes é simulada. A interface Tk também foi exercitada com consulta simulada.

O fluxo de compilação foi executado no Linux com as fontes autenticadas e sem autenticação. Gerou as duas imagens completas e o cliente correspondente à versão autenticada. Foram aprovados 19 testes, incluindo uma aplicação de duas páginas gerada pelo Montador original. Preparar ferramentas também foi executado e repetido no mesmo ambiente.

A compilação sem autenticação apresentou 884 ocorrências de avisos do código/bibliotecas existentes e nenhum erro. A execução autenticada reutilizou o cache e não emitiu novos avisos; isso não significa que uma recompilação completa dela esteja livre de avisos. Nenhuma dessas advertências foi escondida pelo gerenciador. O ZIP inclui o resumo `gerenciador-testes.txt` e os logs completos em `validacao/`.

Não houve gravação em hardware real, teste físico de proteções nem validação em Windows. O programa não afirma que um BIN comum passou a ser protegido após gravá-lo.
