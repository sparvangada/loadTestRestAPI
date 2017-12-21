#!/usr/bin/env python 

import requests
import json
from pprint import pprint
import time
import sys
from datetime import datetime

sys.stdout=open("output.txt","a+")
now = datetime.now()
print("Starting new instance of restApi at %s" % (now))
#def callRestApi():
requestArray = json.load(open('yourJsonFile.json'))

pprint(requestArray)

url='https://hostname:port/yourContextPath'
headers = {'Authorization' : 'yourAuthorization', 'Accept' : 'application/json', 'Content-Type' : 'application/json'}

for singleJson in requestArray:
	pprint(json.dumps(singleJson))
	r = requests.post(url, data=json.dumps(singleJson), headers=headers)
	pprint(r)
	pprint('================================================')
	# Wait for 5 seconds
	time.sleep(10)
