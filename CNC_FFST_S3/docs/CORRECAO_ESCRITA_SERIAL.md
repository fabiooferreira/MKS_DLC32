# Correção de escrita concorrente no Python

O usuário relatou timeout de escrita após iniciar arquivo laser, com autenticação já concluída. O cliente permitia chamadas simultâneas a pyserial.write no mesmo objeto: consultas de status contornavam os locks usados pelo comando assinado. No Windows esse objeto usa uma estrutura overlapped de escrita compartilhada. Essa concorrência foi removida; ainda não se confirmou na placa que ela era a causa do timeout relatado.

Uma trava de transmissão curta protege todas as escritas físicas: handshake, comandos, realtime e fechamento. Consultas `?` são dispensadas se houver escrita em curso; a próxima consulta atualizará o estado. Parada e reset aguardam somente a escrita corrente (timeout existente de 2 s), não a confirmação de movimento ou autenticação. Comandos assinados continuam limitados pela confirmação da placa.

Falha no envio de arquivo cancela o envio, tenta feed hold e preserva a mensagem original de falha. Não há repetição automática de comandos. Com USB indisponível, o envio de feed hold não garante parada física: verifique a máquina e use a emergência física se necessário.

O firmware não mudou: UART/USB 0.1.2 e protegido 0.2.2. Se o BIN correspondente já está instalado, basta trocar o Python. O pacote Serial inclui o BIN por conveniência, sem necessidade de regravar. Não use com BIN antigo de outra versão/perfil.

Teste de regressão força uma escrita bloqueada, consulta de status e parada concorrentes: nenhum acesso simultâneo ao write, status ocupado dispensado e parada enviada após a escrita. A suíte de autenticação tem 23 testes. Testes de interface usam portas simuladas; validação em CH343/Windows e com o arquivo real permanece pendente.
