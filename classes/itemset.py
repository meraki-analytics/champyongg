import champyongg.common


class ItemSet(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.games = dictionary.get('games', 0)
        self.items = dictionary.get('items', [])
        self.role = dictionary.get('role', '')
        self.win_percent = dictionary.get('winPercent', 0.0)

