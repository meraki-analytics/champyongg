import champyongg.common


class SummonerSpellSet(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.games = dictionary.get('games', 0)
        self.role = dictionary.get('role', '')
        self.summoner1 = dictionary.get('summoner1', '')
        self.summoner2 = dictionary.get('summoner2', '')
        self.win_percent = dictionary.get('winPercent', 0.0)

