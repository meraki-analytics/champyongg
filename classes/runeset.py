import champyongg.common


class RuneSet(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.games = dictionary.get('games', 0)
        self.role = dictionary.get('role', '')
        self.runes = [Rune(r) for r in dictionary.get('runes', [])]
        self.win_percent = dictionary.get('winPercent', 0.0)


class Rune(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.description = dictionary.get('description', '')
        self.id = dictionary.get('id', 0)
        self.name = dictionary.get('name', '')
        self.number = dictionary.get('number', 0)

