#This simple script extracts the variable from a json file and returns the sum of the extracted variables.
import json
import urllib.request, urllib.parse, urllib.error
import ssl
url = input('Enter location: ')
if len(url) < 1: quit()
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
uh = urllib.request.urlopen(url, context=ctx).read() #Open and read data from the url
print('Retrieving', url) 
data=uh.decode() #Decode the data
print('Retrieved', len(data), 'characters')
info = json.loads(data) # Load into json
vals =[]
for item in info['comments']:
     vals.append(int(item['count']))
sumvals=sum(vals)
print(sumvals)
