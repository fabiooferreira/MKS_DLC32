# Compilação CNC_FFST 0.3.0 com chave fixa

Build PlatformIO e imagem completa: SUCCESS. Nenhum erro de compilação nesta execução.
884 ocorrências de warning herdados, listadas integralmente em artifacts/warnings.txt; contexto em artifacts/build-full.log.
RAM 69292/327680 bytes (21,1%); flash 1711642/3145728 bytes (54,4%).

| Ocorrências | Mensagem |
| --- | --- |
| 28 | `"TOUCH_CS" redefined` |
| 28 | `narrowing conversion of '(((int)b) >> 3)' from 'int' to 'uint16_t {aka short unsigned int}' inside { } [-Wnarrowing]` |
| 28 | `narrowing conversion of '(((int)g) >> 2)' from 'int' to 'uint16_t {aka short unsigned int}' inside { } [-Wnarrowing]` |
| 28 | `narrowing conversion of '(((int)r) >> 3)' from 'int' to 'uint16_t {aka short unsigned int}' inside { } [-Wnarrowing]` |
| 2 | `no return statement in function returning non-void [-Wreturn-type]` |
| 8 | `control reaches end of non-void function [-Wreturn-type]` |
| 1 | `extra tokens at end of #endif directive [-Wendif-labels]` |
| 1 | `variable 'pwm_value' set but not used [-Wunused-but-set-variable]` |
| 95 | `ISO C++ forbids converting a string constant to 'char*' [-Wwrite-strings]` |
| 2 | `suggest parentheses around assignment used as truth value [-Wparentheses]` |
| 1 | `enumeration value 'PROBE_FINISH' not handled in switch [-Wswitch]` |
| 1 | `'speed' may be used uninitialized in this function [-Wmaybe-uninitialized]` |
| 1 | `'step' may be used uninitialized in this function [-Wmaybe-uninitialized]` |
| 656 | `cast from pointer to integer of different size [-Wpointer-to-int-cast]` |
| 1 | `implicit declaration of function 'malloc' [-Wimplicit-function-declaration]` |
| 1 | `incompatible implicit declaration of built-in function 'malloc'` |
| 2 | `initialization from incompatible pointer type [-Wincompatible-pointer-types]` |

A base original oculta warnings com -w; o perfil CNC_FFST mantém os warnings habilitados. Avisos herdados não foram corrigidos nem ocultados nesta tarefa. Não considerar firmware de produção validado por causa da compilação.

## Verificações

- 11 testes host com FFSTAuth.cpp real e transporte Python: aprovados (auth-host-tests.txt). Shims de RTOS/GPIO/identidade; HMAC OpenSSL no host e mbedTLS no ESP32.
- Sintaxe do programa e módulo Python: verificada com py_compile. GUI/Tk e EXE Windows não executados.
- Comparação AST com o Python original: apenas Streamer.connect, Streamer.realtime e App.connect foram alterados; demais funções/métodos preservados.
- BIN completo 4MB, aplicação no offset correto, checksums/hash ESP32, manifesto/cliente e chave compartilhada embutida: verificados, sem imprimir a chave (auth-artifact-verification.txt).
- EXE Windows: script PyInstaller fornecido; geração não executada neste Linux.
- Testes de bancada USB, rede, movimento, laser, sondagem, limites e segurança: pendentes. O usuário confirmou funcionamento da revisão 0.2.0; isso não valida a nova 0.3.0.

## Diagnósticos durante o desenvolvimento

O teste host inicial de realtime encontrou um aviso de snprintf potencialmente truncado, corrigido com limites explícitos no formato e revalidado com -Werror. Ajustes no harness (isolamento de estado e consumo de respostas) foram corrigidos antes dos resultados finais. A comparação AST inicialmente esperava uma mudança de UI de pareamento; após a opção por chave fixa essa mudança foi removida, e a expectativa do teste foi ajustada. Não há testes host falhando no resultado final.
