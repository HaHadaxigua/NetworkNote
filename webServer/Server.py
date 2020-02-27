from socket import *


def start():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    try:
        serverSocket.bind(('', 8887))
        serverSocket.listen(1)
        while True:
            print("The server is starting")
            connectionSocket, addr = serverSocket.accept()
            try:
                message = connectionSocket.recv(4096)
                print(message.decode())
                filename = message.split()[1]
                f = open(filename[1:])
                outputData = f.read()
                header = 'HTTP/1.1 200 OK\n' \
                         'Connection: close\n' \
                         'Content-Type: text/html; charset=utf-8\n' \
                         'Content-Length: ''%d\n\n' % (len(outputData))
                connectionSocket.send(header.encode('utf-8'))
                for i in range(0, len(outputData)):
                    connectionSocket.send(outputData[i].encode())
                connectionSocket.close()
            except IOError:
                header = 'HTTP/1.1 404 Found'
                connectionSocket.send(header.encode())
            finally:
                connectionSocket.close()
    finally:
        serverSocket.close()


if __name__ == '__main__':
    start()