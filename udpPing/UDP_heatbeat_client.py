from socket import *
import time


def start():
    serverName = '127.0.0.1'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)
    for i in range(10):
        sendTime = time.time()
        message = ('Ping %d %s' % (i + 1, sendTime)).encode()
        try:
            clientSocket.sendto(message, (serverName, serverPort))
            modifiedMessage, addr = clientSocket.recvfrom(1024)
            rtt = time.time() - sendTime
            print('Sequence %d: Reply from %s  RTT = %.3fs' % (i + 1, serverName, rtt))
        except Exception as e:
            print('Sequence %d: Request timed out' % (i + 1))
            print(e)
    clientSocket.close()


if __name__ == '__main__':
    start()
