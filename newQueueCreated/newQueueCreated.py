#!/usr/bin/env python
import requests
from urlparse import *
import os, sys, json
from iron_mq import *

IRON_TOKEN = os.getenv('IRON_TOKEN')

ironmq = IronMQ(host="mq-aws-us-east-1.iron.io",
                project_id="52ba6fcb4c05a60009000001",
                token="IRON_TOKEN",
                protocol="https", port=443,
                api_version=1,
                config_file=None)

def addSubscriberToQueue(q, name, subscriberUrl):
	url = q
        d = {	
	    "push_type": "multicast",
	    "error_queue": name+"error",
	    "subscribers": [
		{
		    "url": subscriberUrl
		}
	    ]
	}
		r = requests.post(url, data=d)
	return r

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
print incomingUrl
ok = parse_qsl(urlparse(u).query, keep_blank_values=True)
print ok
print (ok[0][0])
eventType = (ok[0][1])
networkName = (ok[1][1])
subscriber1 = "https://worker-aws-us-east-1.iron.io:443/2/projects/52ba6fcb4c05a60009000001/tasks/webhook?code_name=pushSceneToChannel&oauth="+IRON_TOKEN
if eventType == "newChannelQueueCreated":
	queue = ironmq.queue(networkName)
	queue.add_subscribers(*[subscriber1])
else:
    print "ko"
