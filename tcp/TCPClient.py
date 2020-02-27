from socket import *

'''
    when use TCP protocol,
    1. creat a socket
    2. connect to server
    3. put data into tcp_connection    
'''


def start():
    serverName = '127.0.0.1'
    serverPort = 8887
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))          # 在python中 需要自己手动的去连接
    print("please entry your lowercase sentence...")
    while True:
        message = input("entry...")
        if message == 'END':
            break
        clientSocket.send(message.encode())
        modifiedMessage = clientSocket.recv(1024)
        print("From Server:", modifiedMessage.decode())
    clientSocket.close()


if __name__ == '__main__':
    start()
