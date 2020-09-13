LIMIT = 3

class Judger():
    def __init__(self):
        self.count = 0

    def judge_whether_tweet(self, trend):
        if not self._is_tweet_count_not_limited():
            return False
        if not self._has_trend_tweet_enough_volume(trend):
            return False
        self.count += 1
        return True

    # Private Method
    def _is_tweet_count_not_limited(self):
        return True if self.count < LIMIT else False

    def _has_trend_tweet_enough_volume(self, trend):
        volume = trend.get('tweet_volume')
        if type(volume) is int and volume > 30000:
            print(f'tweet about {trend.get("name")}')
            return True
        else:
            return False
        
