"""
EECE 350
Assignment 1 - Time Protocole using Socket

Frederic Zein
201900768
"""

import socket
import struct
n=bytes()
server1 = "time-a-wwv.nist.gov"
server2 = "utcnist.colorado.edu"
port = 37
bufferSize = 4096

def timeprint(time):
    timeYears = time // (3600*24*365)
    print("\t", time, "seconds since the year 1900,")
    print("\t which is equivalent to ", timeYears, " years since 1900.")

#Create sockets
mysocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to servers
mysocket1.connect((server1, port))
mysocket2.connect((server2, port))

#Send requests
mysocket1.send(n)
mysocket2.send(n)

#Receive responses and convert from hex to seconds
response_time1 = mysocket1.recv(bufferSize)
timeSeconds1, = struct.unpack('!I', response_time1)

response_time2 = mysocket2.recv(bufferSize)
timeSeconds2, = struct.unpack('!I', response_time2)

#Close sockets
mysocket1.close
mysocket2.close

#Print
print("\nFor server 1:")
print("The IP adress of the server is: 132.163.97.1")
print("And the time retrieved is: ")
timeprint(timeSeconds1)

print("\nFor server 2:")
print("The IP adress of the server is: 128.138.140.44")
print("And the time retrieved is: ")
timeprint(timeSeconds2)

print("\nThe time difference between both servers is: ", abs(timeSeconds2-timeSeconds1), " seconds.\n")
