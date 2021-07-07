
import socket
from _thread import *


def echo(cliente, msg):
  '''
  Recebe a mensagem do cliente e a envia novamente
  '''
  msg = msg.decode('ascii')
  cliente.send(msg.encode('ascii'))


def conexaoThread(cliente, endereco):
  #cliente.send("Conexao estabelecida".encode('ascii'))

  while True:
    cliente.send(
        "Informe o comando que deseja executar(echo/quit):".encode('ascii'))
    comando = str(cliente.recv(1024).decode('ascii'))

    if comando == "echo":
      cliente.send("Digite a mensagem: ".encode('ascii'))
      msg = cliente.recv(1024)
      echo(cliente, msg)
    elif "quit":
      break

  print(f"Conexão com o cliente {endereco} finalizada")
  cliente.close()


if __name__ == '__main__':
  # Criando o socket
  s = socket.socket()

  # IP e Porta do servidor
  host = ''
  porta = 9000

  # Vinculando o socket a porta
  s.bind((host, porta))

  # Colocando o socket em execução
  s.listen(5)
  print(f"Servidor está escutando na porta {porta}")
  while True:

    cliente, endereco = s.accept()

    print(f'Conexao aceita do cliente {endereco}')

    start_new_thread(conexaoThread, (cliente, endereco))

  # Fechando socket
  s.close()
