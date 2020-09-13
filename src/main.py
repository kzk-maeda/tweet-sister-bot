import os
import sys
import time
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), './lib/'))
sys.path.append(os.path.join(os.path.dirname(__file__), './'))

import json
import yaml
from requests_oauthlib import OAuth1Session

from twitter import Twitter
from judger import Judger

# Local Config
WOEID = 1118370
SLEEP_TIME = 10

def lambda_handler(event, context):
    print(event)
    env = event.get('env')
    twitter = Twitter(env=env)
    trends = twitter.get_trends(id=WOEID)
    judger = Judger()
    for trend in trends:
        should_tweet = judger.judge_whether_tweet(trend)
        if should_tweet:
            twitter.post_tweet(trend.get('name'))
            time.sleep(SLEEP_TIME)


# for local debug
if __name__ == "__main__":
    event = {"time": datetime.now().strftime('%Y-%m-%d'), "env": "local"}
    lambda_handler(event=event, context=None) 