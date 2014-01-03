#!/usr/bin/env python
import sys, json, os
from urlparse import *
from iron_mq import *

ironmqCHANNEL = IronMQ(host="mq-aws-us-east-1.iron.io",
                project_id="52ba6fbe61680f0005000001",
                token="rhJuFZcZzPqj48eR471VvDu1O40",
                protocol="https", port=443,
                api_version=1,
                config_file=None)
             
ironmqNETWORK = IronMQ(host="mq-aws-us-east-1.iron.io",
                project_id="52ba6fcb4c05a60009000001",
                token="rhJuFZcZzPqj48eR471VvDu1O40",
                protocol="https", port=443,
                api_version=1,
                config_file=None)


payload = None
payload_file = None
for i in range(len(sys.argv)):
    if sys.argv[i] == "-payload" and (i + 1) < len(sys.argv):
        payload_file = sys.argv[i + 1]
        break
f = open(payload_file, "r")
contents = f.read()
f.close()
try:    
        payload = json.loads(contents)
except ValueError:
        pass
        
u = contents
print u 
incomingUrl = urlparse(u).query
ok = parse_qsl(urlparse(u).query, keep_blank_values=True)
def eventType(o):
        try:
            return o[0][1]
        except (IndexError):
            pass
ko = eventType(ok)
print ko
def networkName(o):
        try:
           return o[1][1]
        except (IndexError):
            pass
def networkEmail(o):
        try:
            return o[2][1] 
        except (IndexError):
            pass
def timestamp(o):
        try:
            return o[3][1]
        except (IndexError):
            pass
queue.delete_queue()
queue1 = ironmqCHANNEL.queue(networkName(ok))
queue1.delete_queue()
