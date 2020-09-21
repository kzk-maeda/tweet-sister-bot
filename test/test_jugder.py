import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from judger import Judger
from dummy_blacklists import DummyBlacklists

THRETHOLD = 30000

def test_tweet_volume_equals_threshold():
    trend = {
        'name': 'dummy',
        'tweet_volume': THRETHOLD 
    }
    judger = Judger()
    judger.blacklists = DummyBlacklists()
    assert not judger.judge_whether_tweet(trend)
    del judger

def test_tweet_volume_lager_than_threshold():
    trend = {
        'name' : 'dummy',
        'tweet_volume' : THRETHOLD + 1
    }
    judger = Judger()
    judger.blacklists = DummyBlacklists()
    assert judger.judge_whether_tweet(trend)