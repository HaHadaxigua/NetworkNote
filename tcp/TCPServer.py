from socket import *

'''
    when use TCP protocol:
    1. create serverSocket and bind local port
    2. wait for new client Connection
    3. creat a new socket for transmission data
    4. after transmission, close the connectionSocket
    5. wait next connect...
    
    this is a simple server, it can only handle one connection,
    ---> MultiThreading
'''


def start():
    serverPort = 8887
    serverSocket = socket(AF_INET, SOCK_STREAM)      # 创建我们的welcomeSocket: 用于tcp握手 (三次握手)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)                           # 等待client连接， 最大连接为1
    print("server is start...")
    connectionSocket, addr = serverSocket.accept()   # 有新的连接进入的话，建立了一个新的ConnectionSocket
    sentence = connectionSocket.recv(1024).decode()  # 从connectionSocket接收消息
    modifiedSentence = sentence.upper()
    print("received from client:", addr)
    connectionSocket.send(modifiedSentence.encode())  # 发送消息
    connectionSocket.close()                          # 发送完毕后关闭连接


if __name__ == '__main__':
    start()
