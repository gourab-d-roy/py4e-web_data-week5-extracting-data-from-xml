import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum=0

url = input('Enter - ')

uh = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(uh)

lst=tree.findall('comments/comment')

for item in lst:
    sum=sum+int(item.find('count').text)

print(sum)
