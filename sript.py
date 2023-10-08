#!/usr/bin/env python3

import socket
import base64


def limit (valor):
    if valor <= 8:
        return (255-(8-valor))
    return valor - 8

ip = "127.0.0.1"
port = 12345

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((ip, port))
bytes_desencriptado = b''
data = b''
read = b''
while True:
    read = client_sock.recv(1024)
    data += read
    ##print("Data:", data)
    if not read:
        break
    read = b''
    client_sock.send(b'OK')

bytes_desencriptado = bytes((byte - 8) for byte in data)
print(bytes_desencriptado.decode())
client_sock.close()
