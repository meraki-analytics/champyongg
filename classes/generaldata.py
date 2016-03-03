import champyongg.common


class GeneralData(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.assists = Assists(dictionary.get('assists', {}))
        self.ban_rate = BanRate(dictionary.get('banRate', {}))
        self.deaths = Deaths(dictionary.get('deaths', {}))
        self.damage_composition = DamageComposition(dictionary.get('dmgComposition', {}))
        self.experience = Experience(dictionary.get('experience', {}))
        self.gold_earned = GoldEarned(dictionary.get('goldEarned', {}))
        self.kills = Kills(dictionary.get('kills', {}))
        self.largest_killing_spree = LargestKillingSpree(dictionary.get('largestKillingSpree', {}))
        self.minions_killed = MinionsKilled(dictionary.get('minionsKilled', {}))
        self.name = dictionary.get('name', '')
        self.overall_position = OverallPosition(dictionary.get('overallPosition', {}))
        self.play_percent = PlayPercent(dictionary.get('playPercent', {}))
        self.role = dictionary.get('role', '')
        self.skills = Skills(dictionary.get('skills', {}))
        self.total_damage_dealt_to_champions = TotalDamageDealtToChampions(dictionary.get('totalDamageDealtToChampions', {}))
        self.win_percent = WinPercent(dictionary.get('winPercent', {}))


class Skills(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.E = E(dictionary.get('E', {}))
        self.Q = Q(dictionary.get('Q', {}))
        self.R = R(dictionary.get('R', {}))
        self.W = W(dictionary.get('W', {}))


class Q(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.name = dictionary.get('name', '')


class W(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.name = dictionary.get('name', '')


class E(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.name = dictionary.get('name', '')


class R(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.name = dictionary.get('name', '')


class Assists(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.change = dictionary.get('change', 0)
        self.position = dictionary.get('position', 0)
        self.val = dictionary.get('val', 0.0)


class BanRate(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.change = dictionary.get('change', 0)
        self.position = dictionary.get('position', 0)
        self.val = dictionary.get('val', 0)


class Deaths(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.change = dictionary.get('change', 0)
        self.position = dictionary.get('position', 0)
        self.val = dictionary.get('val', 0.0)


class DamageComposition(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.magic_dmg = dictionary.get('magicDmg', 0.0)
        self.physical_dmg = dictionary.get('physicalDmg', 0.0)
        self.true_dmg = dictionary.get('trueDmg', 0.0)


class Experience(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.change = dictionary.get('change', 0)
        self.position = dictionary.get('position', 0)
        self.val = dictionary.get('val', 0.0)


class GoldEarned(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.change = dictionary.get('change', 0)
        self.position = dictionary.get('position', 0)
        self.val = dictionary.get('val', 0)


class Kills(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.change = dictionary.get('change', 0)
        self.position = dictionary.get('position', 0)
        self.val = dictionary.get('val', 0.0)


class LargestKillingSpree(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.change = dictionary.get('change', 0)
        self.position = dictionary.get('position', 0)
        self.val = dictionary.get('val', 0.0)


class MinionsKilled(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.change = dictionary.get('change', 0)
        self.position = dictionary.get('position', 0)
        self.val = dictionary.get('val', 0.0)


class OverallPosition(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.change = dictionary.get('change', 0)
        self.position = dictionary.get('position', 0)


class PlayPercent(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.change = dictionary.get('change', 0)
        self.position = dictionary.get('position', 0)
        self.val = dictionary.get('val', 0.0)


class TotalDamageDealtToChampions(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.change = dictionary.get('change', 0)
        self.position = dictionary.get('position', 0)
        self.val = dictionary.get('val', 0)


class WinPercent(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.change = dictionary.get('change', 0)
        self.position = dictionary.get('position', 0)
        self.val = dictionary.get('val', 0.0)


class TotalHeal(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.change = dictionary.get('change', 0)
        self.position = dictionary.get('position', 0)
        self.val = dictionary.get('val', 0.0)


class VisionWardsBoughtInGame(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.change = dictionary.get('change', 0)
        self.position = dictionary.get('position', 0)
        self.val = dictionary.get('val', 0.0)


class WardsKilled(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.change = dictionary.get('change', 0)
        self.position = dictionary.get('position', 0)
        self.val = dictionary.get('val', 0.0)


class WardsPlaced(champyongg.common.ChampyonGGObject):
    def __init__(self, dictionary):
        self.change = dictionary.get('change', 0)
        self.position = dictionary.get('position', 0)
        self.val = dictionary.get('val', 0.0)

