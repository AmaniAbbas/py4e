import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

place_name = input("Enter a place name: ")
base_url = "http://python-data.dr-chuck.net/geojson?sensor=false&"
address_param = urllib.parse.urlencode({'address': place_name})
target = base_url + address_param

print ("Retrieving {0}".format(target))
connection = urllib.request.urlopen(target)
raw_data = connection.read()
print ("Retrieved {0} characters".format(len(raw_data)))
parsed_data = json.loads(raw_data)

#print(parsed_data)
print ("Place id", parsed_data["results"][0]["place_id"])
