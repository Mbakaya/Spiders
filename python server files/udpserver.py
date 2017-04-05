#CpSc 423 Fall 2016
#Code For Client

#usr/bin/env python
#encoding: utf -8
# from _future_import print_function,unicode literals

import re
import sys
import clientsocket
import time
import serversocket
import socket

#introducing the three variables client  time and server

clientName = '127.0.0.10'
#client is assigned a general I.P 

clientSocket = serversocket(AF_INET,SOCK_DGRAM)
#create the socket

clientSocket.settimeout(1)
#sets the timeout at 1 second

sequence_number = 2
#variable to keep track of the sequence number

while sequence_number <=10:

#message to be sent

    start = time.time()
#assigns the variable 
message = 'Ping'  #function for execution

clientSocket.sendto(message,(clientName,8000))
#important function for opening server 8000

message,address = clientSocket.recvfrom(1024)
#assigns the message whether the total time between the ping  and server opening print sequence_number

print 'message'

print 'Round Trip Time is:' + str(elapsed) + "seconds"
#issue with printing elapsed unless it was changed to a string 

except = socket.timeout:
#if socket takes longer than 1 second,it does the following instead of that try 

print 'Sequence_number'

print 'No Connection from client'

sequence_number +=1
#sequence number is increased after all of the other statements in the while

if sequence_number  > 10:
#closes the socket after 10 packets

clientSocket.close()
 