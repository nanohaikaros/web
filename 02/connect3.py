#!/usr/bin/env python
# Inforamtion Example - Chapter 2 - connect3.py

import socket

print "Creating socket...",
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "done."

print "Looking up port number...",
port = socket.getservbyname('http', 'tcp')
print "done."

print "Connecting to reomte host on port %d..." % port,
s.connect(("www.google.com", port))
print "done."

print "Connected from", s.getsockname()
print "Connected to", s.getpeername()