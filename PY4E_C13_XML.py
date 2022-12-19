# This script reads the "comments" XML file, and extracts the "count" variable from each tree
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

address = input('Enter location: ')
print('Retrieving', address)
uh= open(address)
data=uh.read()
print('Retrieved', len(data), 'characters')
tree=ET.fromstring(data)
counts=tree.findall('.//count')
vals=[]
for count in counts:
     vals.append(int(count.text))
sumvals=sum(vals)
print(sumvals)
#     data = uh.read()
#     print('Retrieved', len(data), 'characters')
#     print(data.decode())
#     tree = ET.fromstring(data)

#     results = tree.findall('result')
#     lat = results[0].find('geometry').find('location').find('lat').text
#     lng = results[0].find('geometry').find('location').find('lng').text
#     location = results[0].find('formatted_address').text

#     print('lat', lat, 'lng', lng)
#     print(location)