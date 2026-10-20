# Aceitação em bancada — todos pendentes

Registrar data, revisão PCB, identificação `$I`, hash do BIN, sender/versão,
`$$`, `$+`, `$N`, `$#`, esquema/fotos de ligação e logs completos. Começar com
alimentação de laser/spindle fisicamente desconectada e curso livre reduzido.
Fazer backup antes de qualquer ajuste e conferir configurações NVS existentes.
Nenhum teste abaixo foi executado neste ambiente sem hardware.

| Teste | Critério de aceitação |
| --- | --- |
| Boot sem LCD | Sem crash/watchdog; banner e `$I` CNC_FFST; ALARM inicial; sem movimento/saída de ferramenta espontânea |
| Serial e Wi-Fi | `?`, `$$`, `$I`, `$G`, `$#` respondem em ambas; testar reset, reconexão e ausência de SD |
| Entrada da sonda | `Pn:P` acompanha contato ao GND; aberto/fechado com polaridade conferida, sem movimento |
| Contato prolongado | Sonda fechada >500 ms e depois >5 s, em repouso: sem FIRE/acidente; G38.2 com contato prévio continua gerando ALARM:4 |
| G38.2 com contato | Com ferramentas desligadas, percurso curto e avanço baixo, para no contato, retorna `[PRB:...:1]`, posição repetível |
| G38.2 sem contato | Percurso curto livre, termina com ALARM:5; não retorna sucesso nem aceita continuidade automática |
| Recuperação | Abrir contato, reconhecer causa e só então desbloquear; nenhum desbloqueio automático em reinício |
| Malha PCB | Sender executa vários pontos, retrações e repetições; verificar alturas com referência independente e deriva |
| Limite físico | Conferir polaridade e habilitar `$21` conforme máquina; acionamento em movimento de baixa energia gera ALARM:1 e parada |
| Limite lógico | Com homing calibrado e `$20` habilitado, movimento além do curso é rejeitado/ALARM:2 sem ultrapassar curso |
| Homing | Testar X/Y e documentar ausência de ciclo Z default; não executar homing sem sensores adequados |
| Reset/emergência | Ctrl-X durante movimento e sondagem interrompe ciclo/saídas; botão físico corta energia perigosa independentemente de USB/Wi-Fi |
| Feed hold | `!` e retomada controlada, sem confundir hold com emergência; testar durante sondagem |
| PWM sem ferramenta | Medir GPIO32 em M3/M4/M5, S0, reset e alarme; conferir frequência, duty e ausência de pulsos de partida |
| Laser | Após testes sem energia, testar modo laser `$32`, M3/M4/M5 e parada com intertravamento/enclausuramento apropriados |
| Spindle | Separadamente, com laser desconectado, calibrar `$30/$31`, `$32=0`, partida/parada e falhas |
| Ruído | Repetir contatos/malha com motores e depois ferramenta em condições controladas; nenhuma falsa sonda ou perda de limite |

Exemplo de comando de sondagem somente após validar sinal e direção:
`G21 G91 G38.2 Z-1 F20` e, se o contato foi bem-sucedido, retração curta na direção
segura e restauração explícita do modo G90. Esse exemplo não calibra a máquina;
não o execute se Z- não for a direção correta ou não houver 1 mm livre.
Uma falha de sondagem exige diagnóstico; não envie `$X` em loop para continuar.

Se aparecer FIRE/FLAME, registrar bytes exatos da serial e do sender e comparar
com `$I`. Não considerar resolvido por simplesmente ocultar a mensagem no sender.
