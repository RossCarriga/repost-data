import json
import pprint
import requests

def sample_valid_reddit_response():

	r = requests.get('http://www.reddit.com/r/cscareerquestions/top.json')
	response_json = r.json()

	if 'data' not in response_json:
		print("Trying again")
		response_json = sample_valid_reddit_response()
	return response_json

def save_sample():
	response_json = sample_valid_reddit_response()

	del response_json['data']['children']

	with open('sample_response.json', 'w+') as f:
		json.dump(response_json, f, indent=5)

