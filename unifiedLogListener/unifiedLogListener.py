#!/usr/bin/env python
import requests
from urlparse import *
import os, sys, json
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
subscriberSortScenes = "https://worker-aws-us-east-1.iron.io:443/2/projects/52ba6fbe61680f0005000001/tasks/webhook?code_name=pushSceneToChannel&oauth=rhJuFZcZzPqj48eR471VvDu1O40" 
subscriberCreateChanTable = "https://worker-aws-us-east-1.iron.io:443/2/projects/52ba6fbe61680f0005000001/tasks/webhook?code_name=createChannelTable&oauth=rhJuFZcZzPqj48eR471VvDu1O40" 
subscriberCreateNetworkTable = "https://worker-aws-us-east-1.iron.io:443/2/projects/52ba6fcb4c05a60009000001/tasks/webhook?code_name=createNetworkTable&oauth=rhJuFZcZzPqj48eR471VvDu1O40"
subscriberAddSceneToDB = "https://worker-aws-us-east-1.iron.io:443/2/projects/52ba6fbe61680f0005000001/tasks/webhook?code_name=addSceneToUnifiedScenesTable&oauth=rhJuFZcZzPqj48eR471VvDu1O40"
def newChannelQueueCreated(cName):
	queue = ironmqCHANNEL.queue(cName)
	r = queue.add_subscribers(*[subscriberCreateChanTable, subscriberSortScenes, subscriberAddSceneToDB])
def newNetworkQueueCreated(nName):
	queue = ironmqNETWORK.queue(nName)
	r = queue.add_subscribers(*[subscriberCreateNetworkTable])
def loginError(nName):
	pass
def login(nName):
	pass
def logout(nName):
	pass
def newNetworkSignUpError(nName):
	pass
def newNetworkSignUpSuccess(nName):
	pass
def login(nName):
	pass
def logout(nName):
	pass
def parseApiCall(nName):
	pass
def pushSceneToChannel(cName):
	pass
ok = parse_qsl(urlparse(u).query, keep_blank_values=True)
def eventType(o):
	try:
	    return o[0][1]
	except (IndexError):
            pass
ko = eventType(ok)
print ko
def networkName(ok):
	try:
	   return ok[1][1]
	except (IndexError):
	    pass
def networkEmail(ok):
	try:
	    return ok[2][1] 
	except (IndexError):
	    pass
def channelName(ok):
	try:
	    return ok[2][1]
	except (IndexError):
	    pass
def sceneType(ok):
	try:
	    return ok[4][1] 
	except (IndexError):
	    pass
def sceneUrl(ok): 
	try:
	   return ok[5][1]
	except (IndexError):
	   pass
def sceneName(ok):
	try:
	    return ok[6][1]
	except (IndexError):
	   pass
def sceneDescp(ok):
	try:
	    return ok[7][1]
	except (IndexError):
	   pass
def sceneTag1(ok):
	try:
	   return  ok[8][1]
	except (IndexError):
	   pass
def sceneTag3(ok): 
	try:
	    return ok[9][1]
	except (IndexError):
	    pass
def scenePrice(ok):
	try:
	    return ok[10][1]
	except (IndexError):
	    pass
def scenePriceDnom(ok):
	try:
	    return ok[11][1]
	except (IndexError):
	    pass
def timestamp(ok):
	try:
	    return ok[12][1]
	except (IndexError):
	    pass

action = {'newChannelQueueCreated': (newChannelQueueCreated, channelName), 'newNetworkQueueCreated': (newNetworkQueueCreated, networkName) , 'loginError': (loginError, networkName) ,'parseApiCall': (parseApiCall, networkName), 'newNetworkSignUpError': (newNetworkSignUpError, networkName), 'newNetworkSignUpSuccess': (newNetworkSignUpSuccess, networkName) , 'login': (login, networkName), 'logout': (logout, networkName), 'pushSceneToChannel': (pushSceneToChannel, channelName)}
print ok
handler, getter  = action.get(eventType(ok))
handler(getter(ok))
  
