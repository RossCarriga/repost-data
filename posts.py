import json
import pprint
import requests

SAMPLE_REDDIT_URL = 'http://www.reddit.com/r/cscareerquestions/top.json'

def sample_valid_reddit_response(url):
	r = requests.get(url)
	response_json = r.json()

	if 'data' not in response_json:
		print("Trying again")
		response_json = sample_valid_reddit_response(url)
	return response_json

def save_sample():
	response_json = sample_valid_reddit_response(SAMPLE_REDDIT_RESPONSE)

	del response_json['data']['children']

	with open('sample_response.json', 'w+') as f:
		json.dump(response_json, f, indent=5)

def get_next_reddit_response():
    response = {}
    with open('sample_response.json', 'r') as f:
        response = json.load(f)
    
    after = response['data']['after']
    response_json = sample_valid_reddit_response(SAMPLE_REDDIT_URL + '?after=' + after)
    del response_json['data']['children']

    print(response_json)

if '__main__' == __name__:
	get_next_reddit_response()
