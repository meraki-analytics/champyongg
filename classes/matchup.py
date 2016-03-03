import champyongg.common


class Matchup(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.games = dictionary.get('games', 0)
        self.key = dictionary.get('key', '')
        self.stat_score = dictionary.get('statScore', 0.0)
        self.win_rate = dictionary.get('winRate', 0.0)
        self.win_rate_change = dictionary.get('winRateChange', 0.0)

