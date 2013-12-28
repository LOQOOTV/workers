#!/usr/bin/env python

from requests import *
from iron_mq import *
import urlparse, os

        def addSubscriberToQueue(self, queue, networkName, subscriber):
                url = queue
		d = {'push_type': "multicast", 'error_queue': networkName+'Error', 'subscribers': [{"url": subscriberPushSceneToChannel}] }
                r = requests.delete(url, data=d)

IRON_TOKEN = os.getenv('IRON_TOKEN')
ironmq = IronMQ(host="mq-aws-us-east-1.iron.io",
                project_id="52ba6fcb4c05a60009000001",
                token=IRON_TOKEN,
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
incomingUrl = urlparse(u)
print incomingUrl
q = incomingUrl.parse_qs
print q
print q['eventType']
//get networkName
queue = 'https://mq-aws-us-east-1.iron.io/projects/1/52ba6fcb4c05a60009000001/queues/%s?oauth=rhJuFZcZzPqj48eR471VvDu1O40'%s networkName
subscriberPushSceneToChannel = 'https://worker-aws-us-east-1.iron.io:443/2/projects/52ba6fcb4c05a60009000001/tasks/webhook?code_name=pushSceneToChannel&oauth=rhJuFZcZzPqj48eR471VvDu1O40'
addSubscriberToQueue(self, queue, networkName, subscriberPushSceneToChannel)
