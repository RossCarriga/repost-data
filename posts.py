import json
import pprint
import requests

SAMPLE_REDDIT_URL = 'http://www.reddit.com/r/cscareerquestions/top.json'

def sample_valid_reddit_response():
	r = requests.get(SAMPLE_REDDIT_URL)
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

def get_next_reddit_response():
    response = {}
    with open('sample_response.json', 'r') as f:
        response = json.load(f)
    
    after = response['data']['after']

    print(after)


if '__main__' == __name__:
	get_next_reddit_response()
