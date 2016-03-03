import champyongg.common


class SkillSet(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.games = dictionary.get('games', 0)
        self.order = dictionary.get('order', [])
        self.role = dictionary.get('role', '')
        self.win_percent = dictionary.get('winPercent', 0.0)

