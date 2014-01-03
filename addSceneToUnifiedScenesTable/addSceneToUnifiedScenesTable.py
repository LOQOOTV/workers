#!/usr/bin/env python
import boto.dynamodb
import os, sys, json, hashlib
from urlparse import *

AWS_SECERT_KEY = "VHcWLK+BwoYxiDZBMKmeT8pxn6sG57VWWFjc4eu4"
AWS_ACCESS_KEY_ID = "AKIAIQSZ745KWSF2QCMA"

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
networkEmail = (ok[2][1]) 
channelName = (ok[3][1]) 
sceneType = (ok[4][1]) 
sceneUrl = (ok[5][1]) 

sceneName = (ok[6][1]) 
if sceneName == "":
   sceneName = "#makeAscene"
else:
   pass
sceneDescp = (ok[7][1]) 
if sceneDescp == "":
   sceneDescp = "loqootv"
else:
   pass
sceneTag1 = (ok[8][1]) 
if sceneTag1 == "":
   sceneTag1 = "noTag"
else:
   pass
sceneTag3 = (ok[9][1])
if sceneTag3 == "":
   sceneTag3 = "noTag"
else:
   pass
scenePrice = (ok[10][1]) 
if scenePrice == "":
   scenePrice = "$0"
else:
   pass
scenePriceDnom = (ok[11][1])
if scenePriceDnom == "":
   scenePriceDnom = "ltv"
else:
   pass
print (ok[13][1])
timestamp = int((ok[13][1]))
networkAvatar = (ok[12][1])
if networkAvatar == "":
   networkAvatar = "http://loqoonet.com/loqootv/LTVlogo.png" 
else:
   pass
from simpleflake import simpleflake, parse_simpleflake
sceneID = simpleflake()
fromGeo = "Test"
conn = boto.dynamodb.connect_to_region(
        'us-east-1',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECERT_KEY)
table = conn.get_table("unifiedScenes")
item_dict = {
		"eventType": eventType, 
		"timestamp": timestamp,
		"networkName": networkName,
		"channelName": channelName,
		"sceneType": sceneType,
		"sceneUrl": sceneUrl,
		"sceneName": sceneName,
		"sceneDescp": sceneDescp,
		"sceneTag1": sceneTag1,
		"sceneTag2": sceneTag3,
		"scenePrice": scenePrice,
		"scenePriceDnom": scenePriceDnom,
		"fromGeo": fromGeo,
		"networkAvatar": networkAvatar,
		"sceneID": sceneID
		}
item1 = table.new_item(attrs = item_dict)
item1.put()
