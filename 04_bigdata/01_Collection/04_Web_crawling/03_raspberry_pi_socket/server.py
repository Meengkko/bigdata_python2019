from socket import *

server_ip = '192.168.0.4'
port = 8080

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind((server_ip, port))
serverSock.listen(1)

print('Server(%s) is waiting on %d port...' % (server_ip, port))

connectionSock, addr = serverSock.accept()

while True:
    try:
        recvData = connectionSock.recv(1024).decode('utf-8')
        print('Receive Command : %s' % recvData)
        if recvData == 'q':
            connectionSock.send('close'.encode('utf-8'))
            connectionSock.close()
            break
        connectionSock.send('Receive OK'.encode('utf-8'))
    except Exception as e:
        print(e)

print('Server it shutdown')
