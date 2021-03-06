# Trabalho de Redes de Computadores - DCC042 - UFJF

## Como executar: 
É possível executar esse projeto de duas formas:
### Em seu localhost:
  1. Abra dois terminais
  2. Em um deles execute <code>python servidor/servidor.py</code>
  3. No outro execute <code>python cliente/cliente.py</code>
### Por meio do Docker:
A execução pelo Docker foi implementada para simular a comunicação entre computadores de uma mesma rede.
Ao usar esse ambiente, os seguintes containers são criados:
<table>
  <tr>
    <td>NOME DO CONTAINER</td>
    <td>IP</td>
  </tr>
  <tr>
    <td>servidor</td>
    <td>192.168.10.2</td>
  </tr>
  <tr>
    <td>cliente1</td>
    <td>192.168.10.10</td>
  </tr>
  <tr>
    <td>cliente2</td>
    <td>192.168.10.20</td>
  </tr>
  <tr>
    <td>cliente3</td>
    <td>192.168.10.30</td>
  </tr>
</table>

Com o docker instalado na sua máquina junto com o docker-compose, siga os passos:
1. Execute <code>docker-compose up</code> na raiz do projeto.
2. Em um terminal para cada máquina cliente execute:
    ```
    docker exec -it NOME_DO_CONTAINER /bin/bash
    python cliente.py
    ```
### Comandos para o servidor
  1. **echo**: ao receber esse comando, o servidor espera o cliente mandar uma mensagem que será replicada.
  2. **quit**: o servidor encerra a conexão com o cliente.

Qualquer comando diferente o servidor irá encerrar a conexão com o cliente.



