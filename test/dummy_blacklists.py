class DummyBlacklists():
    def __init__(self):
        pass

    def is_blacklisted(self, word):
        blacklist_words = [
            'trend_blacklisted_A',
            'trend_blacklisted_B'
        ]
        if word in blacklist_words:
            return True
        else:
            return False
