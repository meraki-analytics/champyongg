import champyongg.common


class Champion(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.key = dictionary.get('key', '')
        self.last_updated = dictionary.get('lastUpdated', 0)
        self.name = dictionary.get('name', '')
        self.roles = {r['name']: Role(r) for r in dictionary.get('roles', [])}


class Role(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.games = dictionary.get('games', 0)
        self.name = dictionary.get('name', '')
        self.percent_played = dictionary.get('percentPlayed', 0.0)

