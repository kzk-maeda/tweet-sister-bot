class Judger():
    def __init__(self):
        pass

    def judge_whether_tweet(self, trend):
        # return False
        volume = trend.get('tweet_volume')
        if type(volume) is int and volume > 30000:
            print(f'tweet about {trend.get("name")}')
            return True
        else:
            return False
