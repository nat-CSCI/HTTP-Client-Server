# UDPclient.py
from socket import * #include Python's socket library
import sys
from html.parser import HTMLParser

serverName = '127.0.0.1' #hostname
serverPort = 12000

# Create UDP socket for server
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = 'GET index.html'

clientSocket.sendto(message.encode(), (serverName, serverPort))

receivedMessage, serverAddress = clientSocket.recvfrom(2048)

print(receivedMessage)

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            print("Encountered a start tag:", tag)
            s = attrs[0]
            print('Attribute: ', s[1])
            clientSocket.sendto(s[1].encode(), (serverName, serverPort))


    def handle_endtag(self, tag):
         if tag == 'img':
            print("Encountered an end tag :", tag)

    def handle_data(self, data):
            if data.__contains__("index_files"):
                print("Encountered some data  :", data)

parser = MyHTMLParser()

f = open("index.html",encoding='utf8')
parser.feed(f.read())


