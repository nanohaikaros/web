#!/usr/bin/env python
# Error Handling Example - Chapter 2 - sockererrors.py

import socket, sys

host = sys.argv[1]
textport = sys.argv[2]
filename = sys.argv[3]

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print "Strange error creating socket: %s" % e
    sys.exit(1)

# Try parsing it as a number port number.

try:
    port = socket.getservbyname(textport, 'tcp')
except socket.error as e:
    print "Couldn't find your port: %s" % e
    sys.exit(1)

try:
    s.connect((host, port))
except socket.gaierror as e:
    print "Address-related error connecting to server: %s" % e
    sys.exit(1)
except socket.error as e:
    print "Connection error: %s" % e
    sys.exit(1)

try:
    s.sendall("GET %s HTTP/1.0r\r\n\r\n" % filename)
except socket.error as e:
    print "Error sending data: %s" % e
    sys.exit(1)

while 1:
    try:
        buf = s.recv(2048)
    except socket.error as e:
        print "Error receiving data: %s" % e
        sys.exit(1)
    if not len(buf):
        break
    sys.stdout.write(buf)
