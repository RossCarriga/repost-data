import json
import pprint
import requests

r = requests.get('http://www.reddit.com/r/cscareerquestions/top.json')
response_json = r.json()

with open('sample_response.json', 'w+') as f:
	json.dump(response_json, f, indent=5)
