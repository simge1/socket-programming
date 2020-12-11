import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='192.168.2.137' 
port=4444 
server.bind((host,port))
server.listen(5)

client, addr=server.accept()
print('connection from: ',addr)

while True:
    try:        
        data=input('>>>')
        client.send(data. encode('UTF-8'))
        print((client.recv(1024)).decode('UTF-8'))
    except ConnectionResetError:
        print('error')
        client, addr=server.accept()
        print('connection from: ',addr)
