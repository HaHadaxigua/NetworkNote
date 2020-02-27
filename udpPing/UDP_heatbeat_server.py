# We will need the following module to generate randomized lost packets
import random
from socket import *


def start():
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', 12000))
    print("server is running...")
    while True:
        rand = random.randint(0, 10)
        message, address = serverSocket.recvfrom(1024)
        message = message.upper()
        if rand < 4:
            continue
        serverSocket.sendto(message, address)


if __name__ == '__main__':
    start()