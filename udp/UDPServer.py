from socket import *


def start():
    serverPort = 8887
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('localhost', serverPort))
    print('the server is listen on: %d', serverPort)
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message.decode().upper()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        print('receive message from:', clientAddress, 'content is:', message.decode())


if __name__ == '__main__':
    start()
