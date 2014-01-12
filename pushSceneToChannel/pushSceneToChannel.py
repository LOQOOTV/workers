#!/usr/bin/env python

import json,httplib, urllib
from urlparse import *
import sys, json, re, hashlib


def gravatar(email,default="http://loqoonet.com/loqootv/LTVlogo.png",size=40):
	gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
	gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
	return gravatar_url

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
sceneDescp = (ok[6][1]) 
sceneTag1 = (ok[7][1]) 
sceneTag3 = (ok[8][1]) 
scenePrice = (ok[9][1]) 
scenePriceDnom = (ok[10][1]) 
networkAvatar = (ok[11][1]) 
timestamp = (ok[12][1])  

try:
    profileImage = gravatar(networkEmail)
except(NameError):
    networkEmail = ("helloworld@loqoo.tv")
    profileImage= gravatar(networkEmail)
action = {'originalVideo': {'tv.loqoo.v4.ORIGINAL_VIDEO_SCENE'}, 'originalAudio': {'tv.loqoo.ORIGINAL_AUDIO_SCENE'},
		'originalImage': {'tv.loqoo.v4.ORIGINAL_IMAGE_SCENE'}, 'originalScene': {'tv.loqoo.v4.ORIGINAL_SCENE'},
		'thirdPartyAudio': {'tv.loqoo.v4.THIRDPARTY_AUDIO_SCENE'}, 'thirdPartyVideo': {'tv.loqoo.v4.THIRD_VIDEO_SCENE'},
		'thirdPartyImage': {'tv.loqoo.v4.THIRDPARTY_IMAGE_SCENE'}, 'thirdPartyPlayStore': {'tv.loqoo.v4.THIRDPARTY_PLAYSTORE'},
		'thirdPartyWeb': {'tv.loqoo.v4.THIRDPARTY_WEB_SCENE'}, 'convo': {'tv.loqoo.v4.CONVO'},
		'originalText': {'tv.loqoo.v4.ORIGINAL_TEXT_SCENE'}}
handler = action.get(sceneType)
print handler
xhandler = str(handler)[6:-3]
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/push', json.dumps({
       "channels": [
          channelName 
       ],
       "data": {
         "action": xhandler,
         "url": sceneUrl,
	 "networkName": networkName,
	 "networkAvatar": networkAvatar,
	 "sceneDescp": sceneDescp,
	 "sceneTag1": sceneTag1,
	 "sceneTag3": sceneTag3
       }
     }), {
       "X-Parse-Application-Id": "fBzdHC1OLCMBmOCvzBLAplhvTtT9BvlJepf3qbab",
       "X-Parse-REST-API-Key": "bcgTZa4c7pxyls9k1r59X3B5s4kjF7kofH76nCiH",
       "Content-Type": "application/json"
     })
result = json.loads(connection.getresponse().read())
print result
