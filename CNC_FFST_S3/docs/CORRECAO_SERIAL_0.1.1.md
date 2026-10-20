# Correção de comunicação — UART/USB 0.1.1 e protegido 0.2.1

Sintoma relatado: a placa transmite Emergency Stop, mas não responde a `$I`, `$FFINFO` e à autenticação do programa. O LaserGRBL consegue abrir a porta e ler mensagens; abrir COM não garantia recepção de comandos pela aplicação.

## Origem identificada no código

`ffst_auth_realtime_allowed()` permitia ASCII imprimível e comandos seguros de realtime, mas rejeitava CR (13) e LF (10). O guarda no início de `protocol_enqueue_realtime_command()` consumia esses bytes antes de o driver colocá-los no buffer RX. Sem terminador, o parser nunca executava as linhas recebidas.

A correção permite CR e LF como dados de entrada. Isso não autoriza o conteúdo da linha: os guardas de G-code e comandos de sistema continuam exigindo assinatura para movimento, spindle/laser, homing e jog. Emergência, limites e falha de sondagem não foram desabilitados. Nenhuma mudança de pinagem, inversão de emergência ou eFuse foi feita para contornar a falha.

## Verificações

Foram acrescentados testes na fronteira de recepção, passando bytes pelo filtro C real e por um coletor mínimo de linhas que modela o consumidor do driver. Os três testes novos falharam antes da correção e passaram depois. Os testes anteriores chamavam diretamente o parser de linhas e não detectaram esse erro de transporte.

São cobertos CR, LF e CRLF, identificação durante EStop e handshake sem liberar movimento/homing sem assinatura. A suíte de autenticação tem agora 20 testes. Os testes de host não substituem o ISR UART e o core completo em hardware.

## Atualização da placa reversível

1. Baixar `CNC_FFST_S3_UART_0.1.1_Correcao.zip` e extrair tudo.
2. Desligar energia dos motores, laser e spindle. Fechar LaserGRBL e outros programas da COM8.
3. Abrir o instalador atualizado deste ZIP; selecionar Reversível e `CNC_FFST_S3_0.1.1_UART_FULL_16MB.bin`.
4. Gravar/verificar em 0x0. O BIN completo substitui os dados e configurações da flash; salvar parâmetros anteriores quando possível.
5. Fechar o instalador. Abrir Fabricação Fresa Laser do mesmo ZIP, COM8, 115200 baud.
6. Conferir autenticação e mensagens. A indicação Emergency Stop pode continuar se GPIO17 estiver alto, como ocorre na DevKit sem o condicionamento da carrier. A conexão não deve liberar movimento nessas condições.

O programa de controle antigo verifica o hash do BIN antigo; por isso precisa ser trocado junto do firmware. O instalador novo reconhece os hashes novos. Não usar o instalador antigo para selecionar um BIN desconhecido.

## Se a placa já foi protegida

Não regravar BIN completo plaintext nem repetir provisionamento. Recompilar 0.2.1 com a mesma assinatura e usar a chave AES já guardada para a placa. Como o firmware antigo também descartava Enter, a consulta autenticada necessária ao atualizador pode falhar. Nesse caso é necessário diagnóstico e recuperação assistida pelo modo ROM seguro, com identificação física da placa e as chaves existentes. Esse procedimento de recuperação não é automatizado por esta entrega. Não recomendar novo provisionamento para esse caso.

## Limites

A causa foi demonstrada no código e nos testes de host. Os BINs são compilados, mas a resposta real da placa após a atualização ainda depende de ensaio. A emergência física continua exigindo o circuito de condicionamento e corte externo da proposta. Não ativar proteção permanente para testar esta correção.
