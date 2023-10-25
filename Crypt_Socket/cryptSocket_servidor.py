#!/bin/python

#SERVIDOR

from simplecrypt import encrypt, decrypt
import socket
import time

#definição do IP do servidor
hostname = '127.0.0.1'
port = 5000

#cria uma lista de clientes
clients = []

#criação do socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((hostname, port))
s.setblocking(0)


print ("Server Started.")

while  KeyboardInterrupt:
    try:
        data, addr = s.recvfrom(2048)
        if addr not in clients:
            clients.append(addr) #se o IP do cliente não estiver na lista, este novo cliente é adicionado
        s.sendto(str(data).encode('utf-8'), addr)

        #Recibo da entrega da mensagem criptografada
        print("MENSAGEM CRIPTOGRAFADA:\n")
        print (data)
        #Descriptografando a mensagem
        print("\n MENSAGEM DESCRIPTOGRAFADA")
        descryptdata = decrypt("Fatec123", data)
        descdata = descryptdata
        print(descdata)

        for client in clients:
            s.sendto(data, client)
    except:
        time.sleep(5)
        pass

s.close()
