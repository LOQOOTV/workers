from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.s3.bucket import Bucket
from urlparse import urlparse
import sys, json
from iron_mq import *


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
url = urlparse(u)
b = str(url.netloc)[0:11]   
k = str(url.path)[1:50]
ext = url.path.split(".")[1]
c = S3Connection("AKIAJMHEGJ4MHAW3MZNQ", "6QIulJCW4k7SN0EE+UZ5oL4yBv1+FIK4YOh6YHkm")
bucket = c.lookup(b)
key = bucket.get_key(k)
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
key.copy(key.bucket, key.name, preserve_acl=True, metadata=handler)
ironmq = IronMQ(host="mq-aws-us-east-1.iron.io",
                project_id="528a52aa04b1ba0005000038",
                token="PCZjzFVSqBKKOn2lwfjvSa62S9E",
                protocol="https", port=443,
                api_version=1,
                config_file=None)

queue = ironmq.queue("pushS3Url2Api")
queue.post(contents)
