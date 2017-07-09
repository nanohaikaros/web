#!/usr/bin/env python
# Basoc DNS library example - Chapter 4 - DNS-basic.py

import sys, DNS

query = sys.argv[1]
DNS.DiscoverNameServer()

reqobj = DNS.Request()

answerobj = reqobj.req(name=query, qtype=DNS.Type.ANY)
if not len(answerobj.answers):
    print "Not found."
for item in answerobj.answers:
    print "%-5s %s" % (item['typename'], item['data'])