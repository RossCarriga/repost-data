import pprint
import requests

r = requests.get('http://www.reddit.com/r/cscareerquestions/top.json')
response_json = r.json()

# pprint.pprint(response_json)

