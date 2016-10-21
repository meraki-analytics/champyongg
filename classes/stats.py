from .. import common


class Stats(common.ChampyonGGObject):
    def __init__(self, dictionary):
        print(dictionary)
        self.id = int(dictionary.get('id', 0))
        self.patch = dictionary.get('patch', "")
        self.championsAnalyzed = int(dictionary.get('championsAnalyzed', 0).replace(",",""))
        self.patchHistory = dictionary.get('patchHistory', [])

