# Alterações do instalador e perfil protegido 0.2.0

- Instalador Tk em arquivo único, porta serial, BIN, log, estado, instalação de dependências e tarefas fora da thread da interface. Reversível é o padrão. Confirmação digitada `PROTEGER` para provisionamento permanente; nenhuma operação física foi executada no desenvolvimento.
- Verificação de imagens reconhecidas por SHA256, cabeçalhos S3, SHA/checksum do bootloader e aplicação, tamanho e tabela. A preparação local registra o novo BIN público, sem salvar chaves no registro.
- Novo ambiente `cnc_ffst_s3_n16r8_protected` com configuração própria: Flash Encryption AES-XTS-256 Release, Secure Boot V2 e Secure ROM Download. JTAG bloqueado. O modo de download NÃO é desabilitado completamente. O perfil inicial que desabilitava download foi substituído antes de qualquer publicação/provisionamento.
- Layout protegido: tabela 0x20000; NVS 0x21000; otadata 0x25000; phy 0x27000; aplicação factory 0x30000, 6 MB; grbl 0x630000; storage 0x640000. Cabeçalho do bootloader normalizado para flash 16 MB antes de assinar, padding 64 KB e assinaturas RSA verificadas após geração. Merge usa parâmetros keep para preservar bytes assinados.
- Assinatura local do proprietário, com backup. Chave privada de teste não distribuída; builds protegidos precisam ser preparados pelo proprietário. `FFST_SIGNING_KEY`/`--signing-key` controlam a assinatura; outro arquivo privado já existente não é sobrescrito silenciosamente.
- Provisionamento automático: identifica MAC/flash e exige eFuses sem proteções existentes; gera chave AES exclusiva por MAC e backup antes de burn_key; duas finalidades AES256 com proteções padrão de leitura/escrita; BIN completo no primeiro provisionamento, sem reset automático entre escrita e verificação.
- Atualização via USB: consulta HMAC com nonce e MAC, confere chave local e identidade de assinatura/layout, criptografa aplicação assinada no host e escreve somente esse ciphertext em 0x30000. Sem novos eFuses. O uso interno restrito de --force serve somente ao ciphertext de atualização, nunca ao BIN plaintext completo.
- `$FFSEC=<nonce>` no perfil protegido: relatório HMAC de estados reais via APIs/eFuses do IDF, MAC, hash do aplicativo e disponibilidade de manutenção. Não fornece conteúdos de chaves. O relatório exige nonce novo e o instalador verifica o hash após atualização.
- Firmware, pinagem, HMAC de movimento, configurações mecânicas e proteções da proposta preservados. Normal UART/USB 0.1.0 continuam sem proteção de leitura; protegido 0.2.0 é somente USB/serial. Cliente de controle protegido gerado em arquivo único e vinculado ao hash da sua compilação, embutindo apenas a credencial HMAC e identidade, sem o BIN completo, chaves AES por placa ou chave privada de assinatura.
- Ferramenta de empacotamento exclui chaves, seed, caches, registros locais e BINs protegidos de teste. Pacote inclui fontes necessárias para gerar o BIN com a sua assinatura.

## Erros e avisos encontrados

Durante desenvolvimento: opção CLI incorreta `extract_public_key --output` corrigida para argumento posicional; cópia redundante do mesmo arquivo de bootloader removida; redefinição de BUILD_INFO causava -Werror em mbedTLS e foi corrigida separando a identificação por ambiente. A normalização do cabeçalho foi movida para antes da assinatura para evitar invalidá-la no merge. Nenhum desses resultados intermediários foi provisionado em placa física.

A compilação final e os testes estão registrados em artifacts/validation. Há o aviso herdado stream_json.c: variável c atribuída mas não utilizada. A base ESP-IDF 4.4.3 continua exigindo revisão/ensaio para produção.

## Limitações

Sem ensaio em hardware, no Windows, de leitura física, clonagem, queda de energia ou recuperação. Atualização sobrescreve aplicação única, sem rollback/OTA. Se o aplicativo não iniciar, o fluxo normal de atualização não consegue autenticar e pode exigir recuperação assistida. Não declarar proteção, sondagem ou segurança elétrica validadas por esses testes no computador.
