# UDPserver
from socket import *
from os.path import exists
import sys
import time

##################################
#------- functions/globals ------#
##################################

# Read html file into string
def readHTML(inFile):
	with open(inFile, 'r', encoding='utf8') as htmlfile:
		data = htmlfile.read()
	return data

#########################
#-------Setting up------#
#########################
""" [Command Line Notes]
Format of command line:
    python myserver.py server_port directory_path

0. len(sys.argv) = 3
1. sys.argv[0] = myserver
2. sys.argv[1] = server_port 
3. sys.argv[2] = directory_path
"""
#serverPort = 12000 #Set serverPort
serverPort = int(sys.argv[1]) #Set serverPort with command line args
serverSocket = socket(AF_INET, SOCK_DGRAM) # Create UDP socket
serverSocket.bind(('', serverPort)) # Bind socket to local port number 12000
#path = "C:/Users/natdy/OneDrive/Desktop/HTTP Client Server/HTTP-Client-Server/SampleWebPage/index.html"
path = sys.argv[2] #set the directory path
start_time = time.time()
print('Ready to receive')
index_file = readHTML(path+'/index.html')
lines = index_file.splitlines()

#################################
#--Wait for Index.html request--#
#################################
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    if "index.html" in message.decode("utf-8"):
        # if exists(path):
         newMessage = "Got it"
         for x in lines:
            serverSocket.sendto(x.encode("utf-8"),clientAddress)
         break
serverSocket.sendto("Done".encode(),clientAddress)
###############################
#----Image/Source Requests----#
###############################
#[Outline for recieving requests]
while 1:
    tag, serverAddress = serverSocket.recvfrom(2048)
    tag = tag.decode()
    print(tag)
    if(tag == "/html"):
        break
    elif(tag=='img'):
        attribute, serverAddress = serverSocket.recvfrom(2048)
        f = open(path+attribute,encoding='utf8')

        #find resource using path
        #send resource to server


########################
#----Finish Program----#
########################
elapsed_time = time.time() - start_time
print('Elapsed Time: ' + elapsed_time)
sys.exit("-----")

