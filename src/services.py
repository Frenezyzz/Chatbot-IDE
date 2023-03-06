import json
import requests

def get_joke():
    url = 'http://some-random-api.ml/joke'
    r = requests.get(url)
    data = r.json()
    return data['joke']

def fetch_apikey(api):
    with open('data/credentials.json') as f:
        data = json.load(f)
    key = data.get(api,None)

    return data[api]

def chatbot(api_key,query):
    url = f"http://api.wolframalpha.com/v1/result?appid={api_key}&i={query}%3f"
    r = requests.get(url)
    data = r.text
    if data == 'Wolfram|Alpha did not understand your input':
        return 'Could\'t understand the query'
    else:
        return data