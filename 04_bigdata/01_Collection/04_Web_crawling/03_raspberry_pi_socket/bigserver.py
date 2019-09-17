from socket import *

server_ip = '192.168.0.7'
port = 8080
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((server_ip, port))

print('Connecting to the server(%s) on %d port' % (server_ip, port))

menu = '''
1. 공원 개장
2. 시뮬레이션 모드
3. 사용자 모드(공연 빅데이터)
4. 종료
'''

while True:
    sendData = input(menu)
    clientSock.send(sendData.encode('utf-8'))
    recvData = clientSock.recv(1024).decode('utf-8')
    print('서버: ', recvData)
    if recvData == '3':
        print('Server notify that server is over')
        break
clientSock.close()
print('Client is shutdown')
