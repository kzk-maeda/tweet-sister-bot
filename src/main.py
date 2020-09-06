import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), './lib/'))
sys.path.append(os.path.join(os.path.dirname(__file__), './'))

import json
import yaml
from requests_oauthlib import OAuth1Session

from twitter import Twitter
from judger import Judger


def lambda_handler(events, contexts):
    twitter = Twitter()
    trends = twitter.get_trends(id=1118370)
    judger = Judger()
    for trend in trends:
        should_tweet = judger.judge_whether_tweet(trend)
        if should_tweet:
            twitter.post_tweet(trend.get('name'))


# for local debug
if __name__ == "__main__":
   lambda_handler(events=None, contexts=None) 