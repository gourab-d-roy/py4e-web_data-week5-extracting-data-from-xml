import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum=0

url = input('Enter - ')

uh = urllib.request.urlopen(url, context=ctx).read()


info = json.loads(uh)
#print('User count:', len(info))
#com=info[0]
for item in info['comments']:
    sum=sum+int(item['count'])

print(sum)
