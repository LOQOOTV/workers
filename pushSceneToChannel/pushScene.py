#!/usr/bin/env python

import json,httplib, urllib
from urlparse import urlparse
import sys, json, re, hashlib

def hay(begin, end, astring):
       i = re.search(begin+'(.*)'+end, astring)
       r = i.group(1)
       return r

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
print contents
networkName = hay("networkName:", ";type", u)
networkEmail = hay("networkEmail:", ";", u )
sceneType = hay("type:", ";sceneUrl:", u)
sceneUrl = hay("sceneUrl:", ";sceneName:", u)
sceneName = hay("sceneName:", ";sceneDescp", u)
sceneDescp = hay("sceneDescp:", ";sceneTag1", u)
sceneTag1 = hay("sceneTag1:", ";sceneTag3", u)
sceneTag3 = hay("sceneTag3:", ";scenePrice", u)
print sceneTag3
scenePrice = hay("scenePrice:", ";scenePriceDnom", u)
scenePriceDnom = hay("scenePriceDnom:", ";sendToChannel", u)
sendToChannel = hay("sendToChannel:", ";networkEmail", u)
try:
    profileImage = gravatar(networkEmail)
except(NameError):
    networkEmail = ("helloworld@loqoo.tv")
    profileImage= gravatar(networkEmail)
action = {'originalAudio': {'tv.loqoo.v4.ORIGINAL_VIDEO_SCENE'}, 'originalVideo': {'tv.loqoo.v4.ORIGINAL_AUDIO_SCENE'},
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
          sendToChannel 
       ],
       "data": {
         "action": xhandler,
         "url": sceneUrl,
       }
     }), {
       "X-Parse-Application-Id": "fBzdHC1OLCMBmOCvzBLAplhvTtT9BvlJepf3qbab",
       "X-Parse-REST-API-Key": "bcgTZa4c7pxyls9k1r59X3B5s4kjF7kofH76nCiH",
       "Content-Type": "application/json"
     })
result = json.loads(connection.getresponse().read())
print result
