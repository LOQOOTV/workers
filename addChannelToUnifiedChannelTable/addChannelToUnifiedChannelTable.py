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
networks = (ok[1][1])  
channelName = (ok[3][1]) 
if eventType == "newChannelAddedToNetwork":
    from simpleflake import simpleflake, parse_simpleflake
f isinstance(obj, set):    channelID = simpleflake()
    conn = boto.dynamodb.connect_to_region(
        'us-east-1',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECERT_KEY)
table = conn.get_table("unifiedChannels")
item
item_dict = {
		"lastUpdated": timestamp,
		"networks": networks,
		"channelName": channelName,
		"lastScene": lastScene,
		"channelID": channelID
		}
item1 = table.new_item(attrs = item_dict)
item1.put()
