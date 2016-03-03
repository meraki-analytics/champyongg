import champyongg.requests
from champyongg.common import ChampyonGGObject
from champyongg.classes.champion import Champion
from champyongg.classes.generaldata import GeneralData, Skills
from champyongg.classes.itemset import ItemSet
from champyongg.classes.matchup import Matchup
from champyongg.classes.runeset import RuneSet
from champyongg.classes.skillset import SkillSet
from champyongg.classes.summonerspellset import SummonerSpellSet


def set_api_key(key):
    """Set your API key
    key    str    the key to use
    """
    champyongg.requests.api_key = key


def print_calls(on):
    """Sets whether to print calls to stdout as they are made
    on    bool    the region to query against
    """
    champyongg.requests.print_calls = on


def get_champions():
    """return    http://api.champion.gg/docs/#api-Champion-GetChampions"""

    request = 'champion'
    return {datum['key']: Champion(datum) for datum in champyongg.requests.get(request)}


def get_general_data(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionGeneralData
    """

    request = 'champion/{name}/general'.format(name=champion)
    return {datum['name']: GeneralData(datum) for datum in champyongg.requests.get(request)}


def get_matchups_by_role(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMatchups
    """

    request = '/champion/{name}/matchup'.format(name=champion)
    return {dictionary['role']: {datum['key']: Matchup(datum) for datum in dictionary['matchups']} for dictionary in champyongg.requests.get(request)}


def get_most_popular_items(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostPopularItems
    """

    request = '/champion/{name}/items/finished/mostPopular'.format(name=champion)
    return {datum['role']: ItemSet(datum) for datum in champyongg.requests.get(request)}


def get_most_popular_skills(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostPopularSkill
    """

    request = '/champion/{name}/skills/mostPopular'.format(name=champion)
    return {datum['role']: SkillSet(datum) for datum in champyongg.requests.get(request)}


def get_most_popular_starting_items(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostPopularStartingItems
    """

    request = '/champion/{name}/items/starters/mostPopular'.format(name=champion)
    return {datum['role']: ItemSet(datum) for datum in champyongg.requests.get(request)}


def get_most_popular_summoners(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostPopularSummoners
    """

    request = '/champion/{name}/summoners/mostPopular'.format(name=champion)
    return {datum['role']: SummonerSpellSet(datum) for datum in champyongg.requests.get(request)}


def get_most_popular_runes(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostPopularRunes
    """

    request = '/champion/{name}/runes/mostPopular'.format(name=champion)
    return {datum['role']: RuneSet(datum) for datum in champyongg.requests.get(request)}


def get_most_winning_items(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostWinningItems
    """

    request = '/champion/{name}/items/finished/mostWins'.format(name=champion)
    return {datum['role']: ItemSet(datum) for datum in champyongg.requests.get(request)}


def get_most_winning_starting_items(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostWinningStartingItems
    """

    request = '/champion/{name}/items/starters/mostWins'.format(name=champion)
    return {datum['role']: ItemSet(datum) for datum in champyongg.requests.get(request)}


def get_most_winning_summoners(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostWinningSummoners
    """

    request = '/champion/{name}/summoners/mostWins'.format(name=champion)
    return {datum['role']: SummonerSpellSet(datum) for datum in champyongg.requests.get(request)}


def get_most_winning_runes(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostWinningRunes
    """

    request = '/champion/{name}/runes/mostWins'.format(name=champion)
    return {datum['role']: RuneSet(datum) for datum in champyongg.requests.get(request)}


def get_most_winning_skills(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostWinningSkill
    """

    request = '/champion/{name}/skills/mostWins'.format(name=champion)
    return {datum['role']: SkillSet(datum) for datum in champyongg.requests.get(request)}


def get_skills(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionSkills
    """

    request = '/champion/{name}/skills'.format(name=champion)
    return Skills(champyongg.requests.get(request))
    #return {key: Skills(datum) for key, datum in champyongg.requests.get(request).items()}


def get_specific_matchup(champion, enemy):
    """champion    <str> champion name
    enemy       <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionSpecificMatchup
    """

    request = '/champion/{name}/matchup/{enemy}'.format(name=champion, enemy=enemy)
    print(champyongg.requests.get(request))
    return {datum['role']: Matchup(datum) for datum in champyongg.requests.get(request)}

