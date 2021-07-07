import os
import socket

# Criando o socket
s = socket.socket()

# IP e Porta do servidor
host = os.environ.get("IP_SERVER") if os.environ.get(
    "IP_SERVER") else 'localhost'
porta = 9000

# Estabelecendo conexão local
s.connect((host, porta))
#msgServidor = s.recv(1024)
# print(str(msgServidor.decode('ascii')))

while True:
  msgServidor = s.recv(1024)
  print(str(msgServidor.decode('ascii')))

  comando = input()
  s.send(comando.encode('ascii'))

  if comando == "echo":
    msgServidor = s.recv(1024)
    print(str(msgServidor.decode('ascii')))

    comando = input()
    s.send(comando.encode('ascii'))

    msgServidor = s.recv(1024)
    print(str(msgServidor.decode('ascii')))
  elif comando == "quit":
    break

# Fechando socket
s.close()
