# Autenticação durante a conexão — 0.1.2 / protegido 0.2.2

Instale BIN e Python correspondentes. Na placa reversível use o pacote UART 0.1.2, COM8 (ou sua porta) e 115200 baud. Não use este BIN normal em placa já protegida. Antes de gravar o BIN completo, salve a saída de `$$`: a imagem completa de 16 MB substitui também a partição das configurações GRBL. Elas ficam na flash, na partição `grbl`, e persistem entre desligamentos; são independentes da sessão de autenticação.

Ao abrir a porta, o Python verifica a identidade exata do firmware, valida a prova HMAC da placa e autentica uma sessão com nonce novo. Cada comando de movimento continua assinado e numerado. Erros normais de G-code e alarmes de segurança não invalidam a autenticação.

Reset de software, reinício da placa e troca de stream invalidam a sessão no firmware. O leitor do Python reconhece o aviso `[FFSESSION:RESET]` ou o banner grbl e autentica novamente na mesma porta. Enquanto isso novos movimentos ficam bloqueados. Um comando pendente sem confirmação é encerrado com erro: não se repete movimento, retomada, desbloqueio ou homing automaticamente. Após recuperar, confira o estado antes de enviar outro comando manualmente.

Ao fechar o programa, `$FFBYE` revoga a sessão quando a porta ainda permite escrita. A UART não detecta de modo confiável todo fechamento físico no computador; por isso a segurança não depende desse aviso: comandos sem assinatura continuam bloqueados, e uma nova abertura pelo programa sempre inicia nonce novo. Falha na renovação bloqueia envios e exige reconexão.

Emergência, limites e falha de sondagem continuam ativos. Renovar autenticação não libera um alarme nem autoriza movimento em Emergency Stop. A interface indica renovação ou autenticação inválida.

Validação automatizada: código C de autenticação executado em host, cliente Python e GUI simulada. Não equivale a ensaio físico da UART/USB, motores, sonda ou emergência. Teste inicialmente sem potência nas ferramentas, verificando conexão, reset, emergência e novo comando deliberado após liberar a condição de segurança. Não considerar aprovado em hardware antes desses ensaios.

## Compilação e verificações

UART 0.1.2, USB 0.1.2 e protegido 0.2.2 compilaram sem erros. Avisos em cada perfil: `stream_json.c:251`, variável `c` atribuída e não utilizada (herdado); cache do pip desativado por falta de permissão no diretório padrão (ambiente). Logs de compilação nos perfis de artifacts; logs de testes em artifacts/validation/session-*.log.

22 testes de autenticação, 7 do instalador e 16 do instalador protegido passaram. Interface Tk simulada passou nos três perfis e dentro do Montador de Páginas, incluindo renovação após reset na mesma porta. Criptografia/assinatura e eFuses virtuais passaram; nenhuma eFuse física foi alterada.
