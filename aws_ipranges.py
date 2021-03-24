#this script pulls regional ip ranges.  change the value for region on the ranges you need.

import requests

#region = 'us-east-1'
region = 'us-west-2'
resp = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json')
d = resp.json()
for i in d['prefixes']:
	if (i['region']) == region:
		print(i['ip_prefix'].strip())
	#print (i) #outputs
    #print(i['ip_prefix'].strip())