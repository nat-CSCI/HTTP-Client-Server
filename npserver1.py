# UDPserver
from socket import *
import sys
serverPort = 12000

# Create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

playing = False

# Bind socket to local port number 12000
serverSocket.bind(('', serverPort))