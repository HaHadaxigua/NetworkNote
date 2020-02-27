from socket import *


tcpSerSock = socket(AF_INET, SOCK_STREAM)  # The Server welcome socket
tcpSerSock.bind(('', 8080))  # bind it to port number 8080
tcpSerSock.listen(1)  # No more users^_^
while True:
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()  # tcpCliSock is the conection socket
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(4096)  # get message from connection socket
    print('The Message received from host is as below:')
    print(message)
    # This message is a HTTP GET request, we need to parse it
    # print message.split()[1] #This is the url requested by browser(preceeded by a '/')
    filename = message.split()[1].partition("/")[2]  # Nothing else, just delete the '/'
    print('The file name is: ' + filename.decode())
    fileExist = "false"  # Initialize it to false
    filetouse = "/" + filename  # WTF does this sentence mean?
    print('The filetouse is: ' + filetouse)
    try:
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        # I think the following 2 sentences are useless
        # tcpCliSock.send("HTTP/1.1 200 OK\r\n")
        # tcpCliSock.send("Content-Type:text/html\r\n")
        # I am wondering whether we should add a 'charset' header here
        for i in range(len(outputdata)):
            tcpCliSock.send(outputdata[i])
        print('Read from cache')
    except IOError:
        if fileExist == "false":
            c = socket(AF_INET, SOCK_STREAM)
            serverName = filename.partition("/")[0]  # The name of Server
            try:
                c.connect((serverName, 80))
                c.send(message)
                # Read the HTTP
                buf = c.recv(4096)
                tmpFile = open("./" + filename, "wb")
                for i in range(0, len(buf)):
                    tmpFile.write(buf[i])
                    tcpCliSock.send(buf[i])
                c.close()  # do not forget to close the client TCP socket
                tmpFile.close()
            except:
                print('Illegal request')
                c.close()
        else:
            print('I do not know what happened now but something bad must happened')
    tcpCliSock.close()

tcpSerSock.close()
