# UDPclient.py
from socket import * #include Python's socket library
import sys

serverName = '127.0.0.1' #hostname
serverPort = 12000

# Create UDP socket for server
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = 'GET index.html'

clientSocket.sendto(message.encode(), (serverName, serverPort))

receivedMessage, serverAddress = clientSocket.recvfrom(2048)

print(receivedMessage)

