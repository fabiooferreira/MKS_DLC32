# Investigação FIRE/FLAME e sondagem

## Evidências nesta base

Uma busca em todas as fontes da aplicação não encontra alarme, pino ou rotina de
detecção FIRE/FLAME. `Exec.h` enumera alarmes 1–10: limites, aborto, sonda, homing
e controle de spindle. Não há alarme de chama nessa enumeração.

`Probe.cpp` contém dois mecanismos distintos:

1. `probe_init`, `probe_get_state`, `set_probe_direction`, `probe_state_monitor`:
   sondagem GRBL, usada por G38.x, monitorada no ISR de passos. Mantida intacta.
2. Monitor legado `mks_probe_check`, que interpreta nível baixo em `PROBE_PIN`
   por 500 ms como acidente, envia reset durante Cycle/Hold e mostra
   `Machine accident`. Seu estado seguinte envia `M3 S0`.

O monitor legado compartilha GPIO22 com a sonda; se fosse ativado, um contato
normal prolongado poderia ser interpretado como acidente. Isso é uma hipótese
de conflito de função, não causa demonstrada do FIRE relatado. A única referência
a `mks_probe_init` em Grbl.cpp já está comentada, e não existe chamada ativa a
`mks_probe_check` nas fontes fornecidas. Portanto esta rotina não explica, por si
só, uma mensagem FIRE em uma placa rodando exatamente esta base.

## Decisão CNC_FFST

O usuário declarou não ter sensor de chama e pediu remover seus alarmes.
Nenhuma detecção de chama foi adicionada. O bloco legado de acidente sobre
`PROBE_PIN` é excluído por `#ifndef CNC_FFST_BUILD`, impedindo a sua inclusão
acidental como monitor concorrente neste perfil. Não foram mascarados alarmes
GRBL, suprimidas mensagens FIRE na comunicação, alterada polaridade da sonda ou
desativados limites. O bloco original permanece disponível no perfil original.

Não foi aplicado um temporizador de supressão durante G38.2, nem um debounce que
altere posição medida. A sondagem elétrica deve permanecer responsiva e falhar
com ALARM:4 (contato inicial inválido) ou ALARM:5 (sem contato no percurso), conforme GRBL.

## O que falta estabelecer

Ainda faltam `$I` da placa original, mensagem exata, sender/versão, ligação da
sonda e reprodução. Uma mensagem FIRE pode vir de outro firmware ou do sender;
não foi confirmado qual. Não é possível declarar a origem corrigida nem a
ausência de falso alarme em hardware sem essas evidências e testes reais.

GPIO22 usa INPUT_PULLUP e `$6=1` por padrão: contato ao GND é ativo. Verifique com
`?`/`Pn:P` antes de mover. Não aplique tensão externa incompatível com ESP32.
Ruído elétrico, aterramento e isolação da ferramenta precisam ser avaliados na bancada.
