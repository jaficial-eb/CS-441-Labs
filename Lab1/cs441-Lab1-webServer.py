#import socket module
from socket import *
import sys
serverSocket = socket(AF_INET, SOCK_STREAM)

#prepare a server socket

# code here

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = # fill this part
    try:
        message = # fill this part
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = # fill this part
        
        # Send one HTTP header line into socket
        # fill in start
        # fill in end

        # Send the content of the requested file to the client

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.sent("\r\n".encode())

        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        # fill this part

        # Close client socket
        # fill this part

    serverSocket.close()
    sys.exit() # Terminate the program after sending the corresponding data