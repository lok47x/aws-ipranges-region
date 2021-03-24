import requests

region = 'us-west-2'
resp = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json')
d = resp.json()
for i in d['prefixes']:
	if (i['region']) == region:
		print(i['ip_prefix'].strip())
