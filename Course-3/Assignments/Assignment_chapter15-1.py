import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
address = urllib.request.urlopen(url)
data = address.read()

print('Retrieving', url)
print('Retrieved', len(data), 'characters')

info = json.loads(data)
info = info["comments"]

total = 0

for item in info:
    print("Count: ",item["count"])
    total = total + int(item["count"])
    print("Sum: ", total)

print("Final sum: ", total)
