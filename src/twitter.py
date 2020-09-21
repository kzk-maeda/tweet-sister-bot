import os
import sys
import boto3
import random

sys.path.append(os.path.join(os.path.dirname(__file__), './lib/'))

import json
import yaml
from requests_oauthlib import OAuth1Session

class Twitter:
    def __init__(self, env='local'):
        if env == 'local':
            with open('./conf/credentials.yml', 'r') as yml:
                credentials = yaml.load(yml, Loader=yaml.FullLoader)
            self.customer_key = credentials.get('customer_key')
            self.customer_secret_key = credentials.get('customer_secret_key')
            self.access_token = credentials.get('access_token')
            self.access_token_secret = credentials.get('access_token_secret')
        elif env == 'aws':
            # get keys from Environment encrypted by KMS
            with open('src/conf/encrypted_credentials.yml', 'r') as yml:
                credentials = yaml.load(yml, Loader=yaml.FullLoader)
            self.customer_key = self._decrypt_kms(credentials.get('encrypted_customer_key'))
            self.customer_secret_key = self._decrypt_kms(credentials.get('encrypted_customer_secret_key'))
            self.access_token = self._decrypt_kms(credentials.get('encrypted_access_token'))
            self.access_token_secret = self._decrypt_kms(credentials.get('encrypted_access_token_secret'))
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
        tweet = f'{word}の妹です。{self._second_word()}'
        print(tweet)
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

    def _decrypt_kms(self, encrypted_text):
        kms = boto3.client('kms')
        key_alias = "twitter-key"
        key_id = f"arn:aws:kms:ap-northeast-1:728291782722:alias/{key_alias}"
        try:
            response = kms.decrypt(
                KeyId=key_id,
                CiphertextBlob=encrypted_text
            )
            return response['Plaintext']
        except Exception as e:
            print(e)

    def _second_word(self):
        word_list = [
            'この度は兄がお騒がしてすみません。',
            'この度は兄がお騒がせしてしまい申し訳ありません。',
            '真実を全てお話しします。'
        ]
        return random.choice(word_list)