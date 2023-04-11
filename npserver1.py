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
	with open(inFile, 'r') as htmlfile:
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

serverPort = 3904 #Set serverPort
#serverPort = int(sys.argv[1]) #Set serverPort with command line args
serverSocket = socket(AF_INET, SOCK_DGRAM) # Create UDP socket
serverSocket.bind(('', serverPort)) # Bind socket to local port number 12000
path = "/home/bernmt/csci373/"
#path = sys.argv[2] #set the directory path
start_time = time.time()
print('Ready to receive')
index_file = readHTML(path+'index.html')
lines = index_file.splitlines()

#################################
#--Wait for Index.html request--#
#################################
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    if "index.html" in message.decode():
        # if exists(path):
         newMessage = "Got it"
         for x in lines:
            if x.strip() != "":
                y = x.strip()
                serverSocket.sendto(y.encode('utf-8'),clientAddress)
                print(y)
         break
print("Done")
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
        image = ''
        attribute, serverAddress = serverSocket.recvfrom(2048)
        attribute = attribute.decode()
        if exists(path+attribute):
            image_file = path+attribute
            with open(image_file,'rb') as infile:
                 while True:
                      chunk = infile.read(2048)
                      if not chunk: break
                      serverSocket.sendto(chunk, clientAddress)
        serverSocket.sendto("Done".encode(),clientAddress)

        #binary file sent to client is too big so it needs to be split up
        #Otherwise, everything is working right
        #serverSocket.sendto(image, clientAddress)
    
        #find resource using path
        #send resource to server

########################
#----Finish Program----#
########################
#elapsed_time = time.time() - start_time
#print('Elapsed Time: ' + elapsed_time)
sys.exit("-----")

