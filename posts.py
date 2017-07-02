import json
import pprint
import requests
import pickle
import redis

SAMPLE_REDDIT_URL = 'http://www.reddit.com/r/cscareerquestions/top.json'
REDIS_DB = redis.StrictRedis(host='localhost', port=6379, db=0)


def sample_valid_reddit_response(url):
    r = requests.get(url)
    response_json = r.json()

    if 'data' not in response_json:
        print("Trying again")
        response_json = sample_valid_reddit_response(url)

    # if 'children' in response_json['data']:
    #     del response_json['data']['children']
    else:
        page_count = len(REDIS_DB.keys(pattern='*'))
        response_json = pickle.dumps(response_json)
        REDIS_DB.set(str(page_count), response_json)

    return response_json


# def get_next_reddit_response(sample):
#     response = {}
#     after = sample['data']['after']
#     response_json = sample_valid_reddit_response(SAMPLE_REDDIT_URL + '?after=' + after)
#     return response_json

sample_valid_reddit_response(SAMPLE_REDDIT_URL)
with open('sample_response.json', 'w+') as f:
    response = pickle.loads(REDIS_DB.get(0))
    json.dump(response, f, indent=5)
