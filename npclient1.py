# UDPclient.py
from socket import * #include Python's socket library
import sys
from html.parser import HTMLParser
import sys
import time

##################################
#------- functions/globals ------#
##################################

class MyHTMLParser(HTMLParser):
    #Send request when an img tag is found
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            print("Encountered a start tag:", tag)
            clientSocket.sendto(tag.encode(), (serverName, serverPort))
            s = attrs[0]
            x = s[1]
            x = x[1:]
            print('Attribute: ', x)
            clientSocket.sendto(x.encode(), (serverName, serverPort))
            message, serverAddress = clientSocket.recvfrom(2048) #recieve response from client
            print(x.split('/')[2])
            c = open(x.split('/')[2], 'wb')
            while message != 'done':
                message, serverAddress = clientSocket.recvfrom(2048) #recieve response from client
                c.write(message)
            c.close()

    def handle_endtag(self, tag):
        if tag == 'html':
             print("Encountered an end tag :", tag)
             message = "/html"
             clientSocket.sendto(message.encode(), (serverName, serverPort))



#########################
#-------Setting up------#
#########################
""" [Command Line Notes]
Format of command line:
    python myclient.py server_ip server_port file_name

0. len(sys.argv) = 4
1. sys.argv[0] = myclient
2. sys.argv[1] = server_ip
3. sys.argv[2] = server_port
4. sys.argv[3] = file_name (index.html)
"""
#serverName = '127.0.0.1' #set IP
serverName = sys.argv[1] #hostname with command line args
#serverPort = 12000 #set port
serverPort = int(sys.argv[2]) #set port with command line args
clientSocket = socket(AF_INET, SOCK_DGRAM) # Create UDP socket for server
start_time = time.time()


##########################
#-------GET Request------#
##########################
message = 'GET index.html'
clientSocket.sendto(message.encode("utf-8"), (serverName, serverPort))
f = open("index_file", 'w', encoding="utf-8")
index_file = ''
x = 0
while 1:
    receivedMessage, serverAddress = clientSocket.recvfrom(2048)
    #print(receivedMessage.decode("utf-8")+"\n")
    if receivedMessage.decode("utf-8") != "Done":
        index_file = index_file+receivedMessage.decode("utf-8")+"\n"
        #print(x)
        #print(receivedMessage.decode("utf-8")+"\n")
        x = x+1
    else:
         break

print("Out of while")
#print(index_file)
f.write(index_file)
f.close()


##########################
#-------HTML parser------#
##########################
""" [HTML Parser Notes]
On a starttag img
    send the message 'img' to server
    send the request for referenced file
    receive the referenced file
On a endtag /html
    send the message '/html'
    end program
"""

image_filenames = []

parser = MyHTMLParser()

f = open("index_file", encoding='utf8')
parsedFile = parser.feed(f.read())

"""[Rough code for handling message sending to client]
for x in parsedFile:
	if(x[0] == '/'): #end tag
		serverSocket.sendto(x.encode(), clientAddress) #send the prompt to client
		if(x == '%end'):
			break
		message, clientAddress = serverSocket.recvfrom(2048) #recieve response from client
		modifiedMessage = message.decode()
		updatedfiletext = updatedfiletext + modifiedMessage + " "
	else: #start tag
		updatedfiletext = updatedfiletext + x + " " #stores in updatedfiletext

"""

########################
#----Finish Program----#
########################
#elapsed_time = time.time() - start_time
#print('Elapsed Time: ' + elapsed_time)
sys.exit("-----")