from blacklists import Blacklists
LIMIT = 3
THRETHOLD = 30000

class Judger():
    def __init__(self):
        self.count = 0
        self.blacklists = Blacklists()

    def judge_whether_tweet(self, trend):
        if not self._is_tweet_count_not_limited():
            return False
        if not self._has_trend_tweet_enough_volume(trend):
            return False
        if self._is_blacklisted(trend):
            return False
        self.count += 1
        print(f'tweet count : {self.count}')
        return True

    # Private Method
    def _is_tweet_count_not_limited(self):
        return True if self.count < LIMIT else False

    def _has_trend_tweet_enough_volume(self, trend):
        volume = trend.get('tweet_volume')
        if type(volume) is int and volume > THRETHOLD:
            print(f'tweet about {trend.get("name")}')
            return True
        else:
            return False
        
    def _is_blacklisted(self, trend):
        word = trend.get('name')
        return True if self.blacklists.is_blacklisted(word) else False
