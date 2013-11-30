import sys, json
import requests
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
print contents
go = requests.get("http://api.loqoo.tv:8000/s3?url='%s'"% contents)

