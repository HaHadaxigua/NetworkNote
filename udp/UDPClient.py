from socket import *

from pip._vendor.distlib.compat import raw_input


def start():
    serverName = '127.0.0.1'
    serverPort = 8887
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    while True:
        message = raw_input('Input lowercase sentence:')
        if message == 'end':
            break
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifiedMessage.decode())
    clientSocket.close()


if __name__ == '__main__':
    start()
