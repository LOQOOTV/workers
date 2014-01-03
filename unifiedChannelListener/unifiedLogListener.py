#!/usr/bin/env python
import requests
from urlparse import *
import os, sys, json
from iron_mq import *
import boto.dynamodb

AWS_SECERT_KEY = "VHcWLK+BwoYxiDZBMKmeT8pxn6sG57VWWFjc4eu4"
AWS_ACCESS_KEY_ID = "AKIAIQSZ745KWSF2QCMA"

ironmqCHANNEL = IronMQ(host="mq-aws-us-east-1.iron.io",
                project_id="52ba6fbe61680f0005000001",
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
#subscriberSortScenes = "https://worker-aws-us-east-1.iron.io:443/2/projects/52ba6fbe61680f0005000001/tasks/webhook?code_name=pushSceneToChannel&oauth=rhJuFZcZzPqj48eR471VvDu1O40" 
def connectToDynamo(key, secKey, table):
	conn = boto.dynamodb.connect_to_region(
        'us-east-1',
        aws_access_key_id=key,
        aws_secret_access_key=secKey)
        table = conn.get_table(table)
	return table
	
def newChannelQueueCreated(cName):
    pass
def channelRemovedFromNetwork(cName, time):
	chanTable = connectToDynamo(AWS_ACCESS_KEY_ID, AWS_SECERT_KEY, "unifiedChannels")
try:
    item = chanTable.getitem(
    hash_key=nName)
    item['networks'].remove(cName)
    item['timestamp'] = time
    item.put()
except:
   
def newChannelAddedToNetwork(nName):
	chanTable = connectToDynamo(AWS_ACCESS_KEY_ID, AWS_SECERT_KEY, "unifiedChannels")
try:
    item = chanTable.get_item(
    hash_key=nName)
    item['networks'].add(nName)
    item.put()
except:
    item_data = { 'channelName': nName, 'lastUpdated': timestamp, 'networks': nName }
    item = table.new_item( attrs = item_data )
    item.put()
def login(nName):
	pass
def logout(nName):
	pass
def pushSceneToChannel(cName):
        chanTable = connectToDynamo(AWS_ACCESS_KEY_ID, AWS_SECERT_KEY, "unifiedChannels")
try:
	
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

action = {'newChannelQueueCreated': (newChannelQueueCreated, channelName), 'login': (login, networkName), 'pushSceneToChannel': (pushSceneToChannel, (channelName, timestamp)), 'channelRemovedFromNetwork': (channelRemovedFromNetwork, (channelName, timestamp)), 'newChannelAddedToNetwork': (newChannelAddedToNetwork, (networkName, timestamp)}
print ok
handler, getter  = action.get(eventType(ok))
handler(*getter(ok))
  
