import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from twitter import Twitter

def test_initialize_local():
    twitter = Twitter(env='local')
    assert twitter.customer_key
    assert twitter.customer_secret_key
    assert twitter.access_token
    assert twitter.access_token_secret

def test_get_trends():
    twitter = Twitter(env='local')
