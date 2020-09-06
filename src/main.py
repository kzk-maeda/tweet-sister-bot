import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), './lib/'))

import json
import yaml
from requests_oauthlib import OAuth1Session

class Twitter:
    def __init__(self):
        with open('credentials.yml', 'r') as yml:
            credentials = yaml.load(yml)
        self.customer_key = credentials.get('customer_key')
        self.customer_secret_key = credentials.get('customer_secret_key')
        self.access_token = credentials.get('access_token')
        self.access_token_secret = credentials.get('access_token_secret')

    def get_session(self):
        self.twitter_session = OAuth1Session(
            self.customer_key,
            self.customer_secret_key,
            self.access_token,
            self.access_token_secret
        )
        return self.twitter_session

    def get_trends(self, session, id, is_exclude_hashtag=True):
        url = 'https://api.twitter.com/1.1/trends/place.json'
        params = {}
        params['id'] = id
        if is_exclude_hashtag:
            params['exclude'] = 'hashtags'
        res = session.get(url, params=params)

        print(res.status_code)
        print(json.loads(res.text))

    def post_tweet(self):
        pass


class Judger():
    def __init__(self):
        pass

    def judge_whether_tweet(self):
        pass


def lambda_handler(events, contexts):
    twitter = Twitter()
    session = twitter.get_session()
    twitter.get_trends(session, id=1118370)

# for local debug
if __name__ == "__main__":
   lambda_handler(events=None, contexts=None) 