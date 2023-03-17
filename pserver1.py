from socket import*
serverPort = 1200
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to receive')

while True:
    connectionSocket, address = serverSocket.accept()
    