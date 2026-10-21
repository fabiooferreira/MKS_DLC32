# CNC_FFST-S3 0.1.3 — revisão de comunicação, pausa e retomada

O sintoma relatado foi Comando/Resposta parados em M5/ok depois da conferência, seguido de “Sem confirmação da placa”. A revisão abrangeu o cliente serial, autenticação, fila de confirmações, pausas/ajustes/retomada, interface, núcleo do grblHAL, perfis de compilação, empacotamento e instalador. Não é uma certificação de todo o código upstream ou da máquina física. A origem exata de perda de dados no Windows/CH343 do usuário ainda depende de teste local; os defeitos abaixo foram reproduzidos ou verificados em testes.

## Instalação desta versão

1. Antes de regravar, salve a saída de `$$` e `$#` da placa atual. Guarde também sua configuração/macros do Python. A imagem completa de 16 MB substitui as configurações na flash; não restaure padrões às cegas depois.
2. Descompacte `CNC_FFST_S3_UART_0.1.3_Revisao.zip` em uma pasta nova. Feche todos os programas que usam a COM, inclusive o controle CNC, antes de abrir o instalador.
3. Para sua ESP32-S3 N16R8 pela USB CH343, grave `CNC_FFST_S3_0.1.3_UART_FULL_16MB.bin` pelo instalador atualizado, no modo **Reversível**, endereço 0x0. Use a sua COM, anteriormente COM8. Esta imagem é para ESP32-S3, não para outras famílias.
4. Feche o instalador. Use `Fabricação Fresa Laser.py` deste mesmo pacote, 115200 baud. Requer Python 3.12, pyserial 3.5 e Pillow 11.3.0; os launchers e instalação de dependências estão incluídos.
5. Confira/restaure sua calibração, limites, emergência, sonda e PWM antes de energizar motores/ferramentas. Teste primeiro com potência das ferramentas desligada.

**BIN 0.1.3 e Python novo devem ser usados juntos.** A recuperação ACK1 depende do firmware novo e a identidade exata da aplicação continua sendo verificada. Trocar somente o Python sobre 0.1.2 não basta para esta entrega.

O perfil USB nativo é separado e exige seu BIN/Python correspondentes. Placa já protegida exige atualização assinada/criptografada com as chaves existentes: NÃO gravar este BIN reversível nela. O kit completo `CNC_FFST_S3_Instalador_0.2.3_Revisao.zip` inclui fontes para gerar o perfil protegido 0.2.3 com a chave do proprietário; não inclui chaves privadas nem BIN protegido assinado pela chave de teste da nuvem. Nenhum eFuse físico foi alterado.

## Alterações e justificativas

| Ponto | Alteração | Efeito/limite |
|---|---|---|
| Leitura serial | Remonta linhas até LF, preservando fragmentos e leituras vazias entre timeouts | Um `ok` ou erro dividido não é descartado; limita uma linha a 64 KiB e falha de modo fechado se exceder |
| Status/hold | Usa bytes realtime nativos 0x80/0x82 e retomada assinada 0x81 por trás dos comandos existentes | Não depende de `$39`; evita inserir `?`/`!` em envelopes de sistema com legacy realtime desligado |
| Confirmação perdida | Firmware retém sequência, MAC da solicitação e resultado do último comando; Python consulta ACK1 autenticado | Recupera o resultado sem reenviar o comando original nem gerar movimento novo |
| Confirmação final | Watchdog também observa o último comando quando não existe próxima escrita | Não espera indefinidamente no fim do arquivo; mantém limite padrão de 120 s sem progresso; respeita prazos de sondagem, duração declarada de G4 e Hold/Door com status recente |
| Interface | Campos ao lado da serial usam snapshots atuais; histórico é processado em lotes de até 100 eventos/12 ms | O terminal acumulado não prende a renderização nem volta os campos para uma mensagem velha |
| Macros | Execução física de macros/comandos manuais ocorre em worker, inclusive macro longa sem M0 | A thread da janela continua disponível para controles; não inicia arquivo concorrente com macro ativa |
| Validação prévia | Verifica ASCII, limite de 200 caracteres por comando e buffer antes de começar arquivo/macro | Uma linha inválida no final é recusada antes de movimento, sem descobrir o problema no meio do trabalho |
| Diagnóstico | Registra TX, comando/seq pendentes, tempo de espera, última linha, tamanho de fragmento e recuperações | Mantém erros originais; faz rotação do log após 10 MiB para `.log.1`; não registra chave nem pacote HMAC de movimento |
| Falha de leitura | Tenta feed hold antes de fechar a conexão | É uma tentativa pela comunicação disponível, não garantia de parada física com USB avariada |

Os passos anteriores de correção de Jog (aguardar Idle antes de G4/G92), Destravar, limpeza na reconexão e aviso não modal permanecem. A caixa chama-se **Pausa para Conferência de Posicionamento e Ajuste Fino**; fechar o aviso não retoma. Só **Retornar** autoriza a retomada.

## ACK1: recuperação sem repetição de movimento

O HMAC v1 de abertura e dos comandos continua. Internamente, `$FFACK=<seq>,<desafio>` é uma consulta somente de leitura, feita após 3 s sem confirmação; o usuário não precisa digitá-la. O firmware não executa G-code, não avança sequência e não libera alarmes nessa consulta.

A resposta inclui o resultado do comando, com prova HMAC ligada ao nonce da sessão, desafio aleatório, sequência e MAC do comando original. Uma resposta PENDING tem prova própria e nunca é tratada como sucesso. O cliente aguarda também o terminador da consulta. Um `ok` isolado durante a consulta não libera a fila: pode ser o ACK original atrasado ou o terminador da consulta, por isso fica em quarentena até existir a prova correspondente. Recusa prova inválida, desafio diferente, contexto antigo, resposta truncada e consulta incompleta.

Reset, troca de sessão e BYE invalidam o registro. Se o comando não chegou ao firmware, ele NÃO é reenviado: permanece pendente e o timeout cancela a operação. Perder a confirmação de um erro não converte o erro em sucesso. A consulta não retoma Hold nem repete homing, sonda, jog, spindle ou trajetória. Prazos declarados para sondagens longas são respeitados. Uma pausa nativa M0 em macro pode aguardar Retornar sem expirar como um comando comum; prazo indefinido não é permitido para comandos de movimento.

O prazo não é renovado por um simples rótulo Run: exige mudança de posição reportada. Hold/Door só suspendem a espera com status recente; comunicação perdida continua expirando. Nenhuma dessas esperas retoma a máquina automaticamente.

Como no GRBL normal, ACK de G0/G1 significa que o bloco foi processado/aceito, não necessariamente que o motor chegou ao destino. A conferência continua usando G4 e confirmação Idle para verificar término do movimento. O registro fica apenas em RAM e não gera gravação de flash por comando.

## Proteções e configuração

Pinagem, passos/mm, velocidades máximas, acelerações, limites, entradas de emergência e sonda não foram alterados. Pulsos mínimos de STEP e atraso DIR continuam nos valores de bancada do perfil (5 µs e 2 µs). Nenhuma proteção foi desativada para resolver a comunicação. Comandos de movimento continuam exigindo assinatura; status e parada continuam acessíveis sem assinatura.

A conferência é gerenciada pelo Python, mantendo o grblHAL em Idle com M5 e bloqueando o restante do arquivo. Seus botões/macros de XYZ usam o caminho normal de movimento e depois G92 para manter as coordenadas de trabalho, preservando a contagem física de máquina. Ver [CONFERENCIA_POSICIONAMENTO_XYZ.md](CONFERENCIA_POSICIONAMENTO_XYZ.md).

G92 pode persistir conforme `$384`; o programa não muda automaticamente essa preferência nem apaga uma origem já calibrada. Leia `$#` antes/depois dos ajustes. Desconectar/reconectar limpa execução e filas do programa, não altera a referência física guardada na placa. Homing e redefinições de origem continuam exigindo conferência do operador.

A chave HMAC compartilhada embutida prova posse da credencial, não identidade inviolável do executável. Ela pode ser extraída de um EXE/BIN reversível; esse modelo foi escolhido para compatibilidade. As chaves privadas de assinatura e criptografia das placas protegidas não são distribuídas.

## Validação e limites

Resultado automatizado: 89 testes unitários passaram (25 autenticação, 19 confirmações, 17 alinhamento, 3 envio, 2 campos de status, 7 instalador, 16 instalador protegido), além da janela de conferência, quatro cenários de integração da GUI/Montador, três verificações criptográficas virtuais e nove cenários no núcleo real.

Os testes novos incluem resposta em fragmentos, ACK perdido e atrasado, consulta repetida, comando que nunca chegou, prova forjada, PENDING, terminador perdido, erro de segurança recuperado e reset. Os testes de interface cobrem histórico acumulado, retomada depois da conferência, macros disponíveis após Destravar, desconexão/reconexão e operação junto ao Montador de Páginas.

Foi acrescentado um teste nativo com o **núcleo real deste repositório** (parser, planejador, stepper/state machine e ffst_auth.c) no grblHAL/Simulator fixado em commit. Ele usa chave e hash públicos de teste, não a credencial da produção. Nove cenários incluem arquivos de 200 movimentos e uma macro com M0 nativo: legacy ligado/desligado, respostas fragmentadas, reset/Hold na pausa e perda deliberada do ACK do M5, inclusive junto com fragmentação e na restauração de M5 após Retornar. Também verifica retomada assinada do M0 nativo com legacy realtime desligado. O teste verifica coordenadas finais e ausência de retransmissão de pacotes de movimento. As adaptações do simulador substituem ESP/RTOS/criptografia por pthreads/OpenSSL e NÃO testam o ISR real da ESP32-S3, flash física ou sinal elétrico.

Compilações UART/USB 0.1.3 e protegido 0.2.3 concluídas sem erros. Avisos encontrados: `main/grbl/stream_json.c:251`, variável `c` definida e não usada (código upstream), e cache do pip indisponível por permissão no ambiente de nuvem. Nenhum aviso novo no módulo de autenticação. Logs completos em artifacts por perfil e `review-build.log`, `review-final-build.log`, `review-protected-build.log`. Testes/logs da revisão em `artifacts/validation/review-*.log`, além das reproduções `fragment-before.log`, `native-rt-before.log` e `display-before.log` (falhas esperadas dos clientes anteriores). O procedimento para repetir o teste do núcleo está em `tests/native/README.md`.

Ainda dependem de hardware: Windows/CH343, integridade do cabo/USB, pulsos e sentido dos drivers, calibração, limites/homing, emergência física, precisão da sonda, PWM, rotação/parada mecânica do spindle, laser e ativação/atualização das proteções permanentes. Não se aumentaram baud, avanço ou aceleração sem medir na máquina. A assinatura por linha tem custo de banda; arquivos extremamente segmentados ainda precisam ser avaliados para acabamento. Não há promessa de superioridade de corte com base apenas no simulador.

O filtro upstream de recepção durante gravação física de NVS é outro ponto que exige ensaio na placa: nessa janela ele suprime controles realtime para evitar execução com cache indisponível. Ele não foi trocado por um handler genérico sem validar IRAM/cache. A repetição de consultas de status é somente leitura; não constitui garantia de parada por USB durante falha ou gravação de flash. A emergência física e sua temporização devem ser verificadas independentemente.

## Teste controlado recomendado

Com ferramentas sem potência e máquina em posição segura/referenciada conforme seus limites, execute um arquivo pequeno com M5, movimento curto, M0 sozinho e outro movimento curto. Na conferência, teste primeiro um único toque de X+, depois Y/Z individualmente. Verifique que WPos fica preservado e MPos muda; clique Retornar e confira o deslocamento acumulado no restante da trajetória. Faça novo teste de cancelamento/Hold e emergência física antes de trabalho real. Se ocorrer falha, não repita um deslocamento incerto: guarde `CNC_PCB_diagnostico_GRBL.log` e sua rotação `.log.1` e confira a posição.
