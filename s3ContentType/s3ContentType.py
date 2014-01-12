from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.s3.bucket import Bucket
from urlparse import * 
import sys, json, re
from iron_mq import *

def hay(begin, end, astring):
       i = re.search(begin+'(.*)'+end, astring)
       r = i.group(1)
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
networkEmail = (ok[2][1]) 
channelName = (ok[3][1]) 
sceneType = (ok[4][1]) 
sceneUrl = (ok[5][1]) 
sceneName = (ok[6][1]) 
sceneDescp = (ok[7][1]) 
sceneTag1 = (ok[8][1]) 
sceneTag3 = (ok[9][1]) 
scenePrice = (ok[10][1]) 
scenePriceDnom = (ok[11][1]) 
timestamp = (ok[12][1])  

url = urlparse(sceneUrl)
print url
b = str(url.netloc)[0:11]   
print b
k = str(url.path)[1:50]
print k
ext = url.path.split(".")[1]
c = S3Connection("AKIAJMHEGJ4MHAW3MZNQ", "6QIulJCW4k7SN0EE+UZ5oL4yBv1+FIK4YOh6YHkm")
bucket = c.lookup(b)
print bucket
key = bucket.get_key(k)
print key
fileExt = {'png': {'Content-Type': 'image/png'}, 'jpe': {'Content-Type':'image/jpeg'}, 
    'jpg': {'Content-Type': 'image/jpeg'}, 'png': {'Content-Type': 'image/png'}, 
    'mp4': {'Content-Type': 'video/mpeg'}, 'mp3': {'Content-Type': 'audio/mpeg'}, 
    '3gp': {'Content-Type': 'video/3gpp'}, 'flv': {'Content-Type': 'video/x-flv'}, 
    'flv': {'Content-Type': 'video/x-flv'}, 'html': {'Content-Type': 'text/html'},
    'mov': {'Content-Type': 'video/quicktime'}, 'pdf': {'Content-Type': 'application/pdf'},
    'svg': {'Content-Type': 'image/svg+xml'}, 'tiff': {'Content-Type': 'image/tiff'},
    'torrent': {'Content-Type': 'application/x-bittorrent'}, 'txt': {'Content-Type': 'text/plain'},
    'vcf': {'Content-Type': 'text/x-vcard'}, 'wav': {'Content-Type': 'audio/wav'}, 
    'xml': {'Content-Type': 'text/xml'}, 'js': {'Content-Type': 'application/javascript'},
    'json': {'Content-Type': 'application/json'}, 'md': {'Content-Type': 'text/markdown'},
    'ogg': {'Content-Type': 'application/ogg'}, 'webp': {'Content-Type': 'image/webp'},
    'm4v': {'Content-Type': 'video/mp3'},'eml': {'Content-Type': 'message/rfc822'},
    'amr': {'Content-Type': 'audio/amr'}, '3gpp': {'Content-Type': 'audio/3gp'}}
handler = fileExt.get(ext)
print handler
key.copy(key.bucket, key.name, preserve_acl=True, metadata=handler)
