#!/usr/bin/env python

from requests import *
from urlparse import *
import os, sys, json

IRON_TOKEN = os.getenv('IRON_TOKEN')

def addSubscriberToQueue(self, queue, networkName, subscriber):
	url = queue
	d = {'push_type': "multicast", 'error_queue': networkName+'Error', 'subscribers': [{"url": subscriberPushSceneToChannel}] }
	r = requests.post(url, data=d)

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
if eventType == "newChannelQueueCreated":
	print "Ok"
else:
    print "ko"
networkName = (ok[1][1])
print networkName
#get networkName
queue = ('https://mq-aws-us-east-1.iron.io/projects/1/52ba6fcb4c05a60009000001/queues/%s?oauth=%s'%  (networkName, IRON_TOKEN))
subscriberPushSceneToChannel = ('https://worker-aws-us-east-1.iron.io:443/2/projects/52ba6fcb4c05a60009000001/tasks/webhook?code_name=pushSceneToChannel&oauth=%s'% IRON_TOKEN)
addSubscriberToQueue(self, queue, networkName, subscriberPushSceneToChannel)
