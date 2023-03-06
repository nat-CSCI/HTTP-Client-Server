# UDPserver
from socket import *
from os.path import exists
import sys
serverPort = 12000

# Create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)


# Bind socket to local port number 12000
serverSocket.bind(('', serverPort))
print('Ready to receive')

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    if "index.html" in message.decode():
        # path = "C:/Users/natdy/OneDrive/Desktop/HTTP Client Server/HTTP-Client-Server/SampleWebPage/index.html"
        # if exists(path):
         newMessage = "Got it"
         serverSocket.sendto(newMessage.encode(),clientAddress )
 