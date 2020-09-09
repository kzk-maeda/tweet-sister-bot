import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from judger import Judger


def test_tweet_volume_equals_threshold():
    trend = {
        'name': 'dummy',
        'tweet_volume': 30000 
    }
    judger = Judger()
    assert not judger.judge_whether_tweet(trend)

def test_tweet_volume_lager_than_threshold():
    trend = {
        'name' : 'dummy',
        'tweet_volume' : 30001
    }
    judger = Judger()
    assert judger.judge_whether_tweet(trend)