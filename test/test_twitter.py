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

def test_get_string_as_second_word():
    twitter = Twitter(env='local')
    second_word = twitter._second_word()
    assert type(second_word) is str