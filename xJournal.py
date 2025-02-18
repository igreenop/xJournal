from requests_oauthlib import OAuth1Session
import os
import json

with open("/Users/iangreen/rooted/xBot/journal/cur.txt", 'r') as cur:
    data = cur.read()
filename = "/Users/iangreen/rooted/xBot/journal/" + data.rstrip() + ".txt"
next = int(data) + 1

print("\n\n", filename, "\n\n") 

if not os.path.isfile(filename):
    print(filename)
    with open(filename, 'w') as journal:
        journal.write("did not journal this week")

with open(filename, 'r') as journal:
    tweet_text = journal.read()


with open("/Users/iangreen/rooted/xBot/journal/cur.txt", 'w') as cur:
    cur.write(str(next))

payload = {"text": tweet_text}

consumer_key = 'consumer key here'
consumer_secret = 'consumer secret here'
access_token = 'access token here'
access_token_secret = 'access token'

oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload
)

if response.status_code != 201:
    raise Exception(
        "Request returned an error: {} {}".format(response.status_code, response.text)
    )

print("Response code: {}".format(response.status_code))

json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))
