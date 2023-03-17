from socket import *
serverName = '127.0.0.1' #hostname
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))



##########################
#-------GET Request------#
##########################
message = 'GET index.html'
clientSocket.send(message.encode())
receivedMessage, serverAddress = clientSocket.recvfrom(2048)
print(receivedMessage.decode())

