import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from judger import Judger

THRETHOLD = 30000

sample_trends = [
    {
        'name': 'trend_A',
        'tweet_volume': THRETHOLD - 1
    },
    {
        'name': 'trend_B',
        'tweet_volume': THRETHOLD
    },
    {
        'name': 'trend_C',
        'tweet_volume': THRETHOLD + 1
    },
    {
        'name': 'trend_D',
        'tweet_volume': THRETHOLD + 1
    },
    {
        'name': 'trend_E',
        'tweet_volume': THRETHOLD + 1
    },
    {
        'name': 'trend_F',
        'tweet_volume': THRETHOLD + 1
    }
]

def test_tweet_is_correct():
    judger = Judger()
    for trend in sample_trends:
        should_tweet = judger.judge_whether_tweet(trend)

        if trend.get('name') == 'trend_A':
            assert should_tweet is False
        elif trend.get('name') == 'trend_B':
            assert should_tweet is False
        elif trend.get('name') == 'trend_C':
            assert should_tweet is True
        elif trend.get('name') == 'trend_D':
            assert should_tweet is True
        elif trend.get('name') == 'trend_E':
            assert should_tweet is True
        elif trend.get('name') == 'trend_F':
            assert should_tweet is False