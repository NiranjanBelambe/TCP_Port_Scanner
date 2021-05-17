#!/usr/bin/python

import socket

def portscanner(port):
	if s.connect_ex((host,port)):
		print "Port is closed"
	else:
		print "Port is open"

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=input("Enter the host ip: ")
for port in range(1,100):
	portscanner(port)



