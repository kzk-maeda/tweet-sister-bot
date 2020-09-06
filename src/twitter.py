import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), './lib/'))

import json
import yaml
from requests_oauthlib import OAuth1Session

class Twitter:
    def __init__(self, env='local'):
        if env == 'local':
            with open('./credentials.yml', 'r') as yml:
                credentials = yaml.load(yml, Loader=yaml.FullLoader)
            self.customer_key = credentials.get('customer_key')
            self.customer_secret_key = credentials.get('customer_secret_key')
            self.access_token = credentials.get('access_token')
            self.access_token_secret = credentials.get('access_token_secret')
        elif env == 'aws':
            # TODO: get keys from Environment encrypted by KMS
            pass
        else:
            print('env is invalid')
        self._get_session()

    def _get_session(self):
        self.twitter_session = OAuth1Session(
            self.customer_key,
            self.customer_secret_key,
            self.access_token,
            self.access_token_secret
        )
        return self.twitter_session

    def get_trends(self, id, is_exclude_hashtag=True):
        url = 'https://api.twitter.com/1.1/trends/place.json'
        params = {}
        params['id'] = id
        if is_exclude_hashtag:
            params['exclude'] = 'hashtags'
        try:
            res = self.twitter_session.get(url, params=params)
        except Exception as e:
            print(e)

        print(res.status_code)
        print(json.loads(res.text))

        if res.status_code == 200:
            trends = json.loads(res.text)[0].get('trends')
            return trends
        else:
            return None

    def post_tweet(self, word):
        url = "https://api.twitter.com/1.1/statuses/update.json"
        tweet = f'{word}の妹です。この度は兄がお騒がせしてすみません。'
        params = {"status" : tweet}

        try:
            res = self.twitter_session.post(url, params = params)
        except Exception as e:
            print(e)
        
        if res.status_code == 200: 
            print("Success.")
        else:
            print("Failed. : %d"% res.status_code)
            print(res.text)