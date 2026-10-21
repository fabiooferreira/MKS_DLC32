# Correção da trava de envio e leitura

Durante envio de arquivo, Streamer chamava SignedPort.write mantendo self.lock, também usado pelo leitor de ACKs. SignedPort pode aguardar o ACK anterior, emitido após liberação de espaço no planner ou término de um comando. Enquanto isso, o leitor da aplicação podia parar no mesmo lock ao processar um ACK já recebido, deixando de atualizar status e coordenadas. A indicação aguardando resposta usa a idade do último status processado; sozinha não comprova desconexão física.

A correção usa uma trava independente para preservar a ordem de envio e mantém a trava da fila apenas durante alterações breves. O registro do comando passa a acontecer antes da escrita, evitando perder um ACK imediato. Consultas de configuração, comandos manuais, sondagem e arquivos usam o mesmo mecanismo. O leitor continua recebendo estados enquanto o envio aguarda confirmação. Autenticação e proteções físicas não mudaram; nenhum movimento é repetido automaticamente.

Regressão reproduzida: a segunda escrita é bloqueada enquanto o leitor recebe ACK e status da primeira. No Python anterior, o status não era processado; no corrigido, o status é processado antes de liberar a escrita. Também testados ACK imediato e remoção correta do registro após falha de escrita. A suíte tem três testes de streaming, além de 23 de autenticação e GUI simulada nos três perfis/Montador.

Firmware sem alterações (UART/USB 0.1.2; protegido 0.2.2). Quem já usa o BIN correspondente precisa trocar somente o Python. Usar o pacote Streaming mais recente. O pacote UART destina-se ao modo reversível UART. Placas protegidas usam o Python correspondente gerado localmente.

O usuário ainda está testando sem motores ligados. Não houve validação física deste ajuste na placa. Uma espera legítima em Hold, M0, alarme ou perda de comunicação ainda exige verificar o log e o estado; não desbloquear nem retomar automaticamente. Testar com potência de ferramentas desligada e observar avanço das confirmações/status.
