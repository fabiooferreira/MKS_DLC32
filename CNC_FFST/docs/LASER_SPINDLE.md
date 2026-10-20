# Perfil laser e operação híbrida — 0.2.0

O perfil `cnc_ffst_v2_1` agora tem defaults `Spindle/Type=LASER` e `$32=1`.
`LASER_OUTPUT_PIN` é um alias do GPIO32 original, não uma nova ligação.
O driver PWM continua disponível para o spindle. Laser e spindle não são
comandados independentemente neste projeto: compartilham a saída original.
O usuário confirmou uma chave seletora manual. O firmware não lê sua posição;
a correspondência entre chave e modo deve ser conferida pelo operador.
Ainda é necessário confirmar a ligação elétrica e a isolação proporcionada pela chave.

## Configurações persistidas

Gravar o BIN não apaga NVS. Uma placa que já guardou `Spindle/Type=PWM` e `$32=0`
continuará com esses valores até o operador alterá-los. Não apague todas as
configurações para mudar o modo: isso perderia calibração da máquina.

Com a máquina parada, ferramentas sem energia, e após reconhecer com segurança
o ALARM de partida quando necessário, enviar comandos individualmente e conferir
`ok` e a leitura de retorno:

```text
M5
$Spindle/Type=LASER
$32=1
$Spindle/Type
$32
$Laser/FullPower
$30
```

O firmware usa `$Laser/FullPower=1000` por padrão no driver laser. Configure no
sender a mesma escala S; confira também `$30`, pois defaults anteriores usam
10000. Para uma operação laser com escala 0–1000, ajuste `$30=1000` de forma
consciente, guardando o valor anterior. Não mande M3/M4 com potência para conferir
configuração; primeiro meça a saída sem alimentar a ferramenta.

## Operação com spindle

Parar o job, enviar M5, cortar energia das ferramentas e selecionar fisicamente
o spindle antes de mudar para `$Spindle/Type=PWM` e `$32=0`. Conferir retorno,
escala S, frequência PWM e controlador reais antes de religar energia.
Para retornar ao laser, repetir a configuração LASER acima com energia cortada.
Nenhum desses comandos seleciona um relé ou garante isolação elétrica.

Esta base MKS tem uma implementação PWM modificada: `calc_pwm_value` usa divisão
fixa por 1000 em vez de mapear diretamente RPM máximas. Não presuma que S10000
representa 10000 RPM corretamente; medir/calibrar a interface do spindle é
obrigatório. Esse comportamento original não foi alterado nesta revisão.

## Validação pendente

Confirmar boot/reconexão sem display, configurações após reiniciar, M3/M4/M5,
PWM durante aceleração/desaceleração e parada em G0/hold/reset/alarme. O driver
LASER habilita os caminhos `inLaserMode()` do parser/stepper quando `$32=1`.
Isso confirma a seleção no código, não valida a potência nem o comportamento
físico. FIRE, sondagem e segurança permanecem sujeitos aos testes de bancada.
