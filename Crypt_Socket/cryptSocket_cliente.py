#!/bin/python

#CLIENTE

from simplecrypt import encrypt, decrypt #import da biblioteca para encriptar

import socket #import da biblioteca para o socket
import threading #import da biblioteca para thread
import time #import da biblioteca utilizada para fazer uma pausa com o sleep

tLock = threading.Lock() #cria threads para executar o programa
poweroff = False

def receving(name, sock):
    while not poweroff:
        try:

            tLock.acquire() #faz o teste na thread, se o retorno é true ele \
                            #continua, se é false ele exibe um erro de timeout expired
            while True:
                data, addr = sock.recvfrom(2048)
                #print (str(data.decode('utf-8')))
        except:
            pass
        finally:
            tLock.release() #se a thread está no estado travado ele destrava e \
                            #passa para a proxima thread, senão ele retorna um erro RunTimeError

#definição do IP do cliente
host = '127.0.0.1'
port = 0

#definição do servidor
server = ('127.0.0.1', 5000)

#criação do socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)
rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()

#definição do nome de usuário (apelido)
alias = input("Username: ")
time.sleep(0.2)

#criação da mensagem e envio para o server
message = input(alias + ">>> ")
while message != 'q':
    cryptmsg = encrypt("Fatec123", message)
    if message != "":
        #s.sendto(str(alias + ": " + cryptmsg).encode('utf-8'), server)
        s.sendto(cryptmsg, server)
        print(cryptmsg)
    tLock.acquire()
    message = input(alias + ">>> ")
    cryptmsg = encrypt("Fatec123", message)
    tLock.release()
    time.sleep(0.2)

#finaliza o socket e o programa
poweroff = True
rT.join()
s.close()
