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

    if 'children' in response_json['data']: 
        del response_json['data']['children']
    else:
        with open('sample_response.json', 'w+') as f:
            json.dump(response_json, f, indent=5)
    return response_json

def get_next_reddit_response(sample):
    response = {}    
    after = sample['data']['after']
    response_json = sample_valid_reddit_response(SAMPLE_REDDIT_URL + '?after=' + after)
    return response_json

def get_all_responses():
    sample = sample_valid_reddit_response(SAMPLE_REDDIT_URL)
    print(sample)
    
    while sample['data']['after'] != "null" and sample['data']['after'] != None:
        sample = get_next_reddit_response(sample)
        print(sample)
    
    print("end")

if '__main__' == __name__:
    get_all_responses()