# Gerenciador ESP32 DLC32 V2.1

Programa em um único arquivo Python, somente para diagnóstico USB. Não altera a autenticação, firmware, pinagem ou eFuses. Não realiza backup nem ativa proteções nesta versão.

1. Instale Python 3.10 ou superior. No Windows, marque Add Python to PATH.
2. Abra o terminal na pasta do arquivo e instale:

```
python -m pip install esptool==4.8.1 bitstring==4.3.1 pyserial==3.5
python Gerenciador_ESP32_DLC32.py
```

3. Pare a máquina, desligue laser/spindle e feche outros controladores. As consultas podem reiniciar a placa.
4. Conecte por USB, selecione a porta e clique em Consultar placa e gerar relatório.
5. Clique em Salvar relatório para enviar. Envie o JSON para preparar a compilação protegida. Não é necessário enviar uma cópia da flash.

O relatório contém MAC, chip/revisão, cristal, tamanho da flash e campos públicos selecionados de segurança. Não contém blocos de chave, conteúdo da flash, senha Wi-Fi nem chave de autenticação. O modelo da placa é uma informação fornecida pelo usuário: o chip não consegue confirmar que a PCB é uma DLC32 V2.1.

Falhas de conexão: confira porta, cabo USB de dados, driver e outros programas usando a serial. Placas com download UART já bloqueado podem não permitir consultas. Nesse caso o programa registra falha, sem tentar mudar as proteções.

A indicação de criptografia ativa representa apenas a paridade do FLASH_CRYPT_CNT; não certifica proteção completa contra extração. O relatório é parte dos dados necessários: ainda é preciso preparar bootloader e aplicação compatíveis, definir atualização/recuperação e validar o procedimento em hardware. O BIN normal atual não se torna compatível simplesmente gravando eFuses. A ativação permanece bloqueada.

Compatível com importação via App(parent) e create_page(parent) no Montador de Páginas. Não precisa de arquivos auxiliares de código.

Verificações realizadas: dependências fixadas, leitura JSON do espefuse virtual, seleção de campos públicos, paridade de criptografia, rejeição de operações fora da lista permitida, identificação e interface Tk com consulta simulada. Não testado em placa física nem no Windows.
