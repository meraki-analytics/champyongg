import pygg.requests
from pygg.common import PyGGObject


def set_api_key(key):
    """Set your API key
    key    str    the key to use
    """
    pygg.requests.api_key = key


def print_calls(on):
    """Sets whether to print calls to stdout as they are made
    on    bool    the region to query against
    """
    pygg.requests.print_calls = on


def get_champions():
    """return    http://api.champion.gg/docs/#api-Champion-GetChampions"""

    request = 'champion'
    return [PyGGObject(datum) for datum in pygg.requests.get(request)]


def get_general_data(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionGeneralData
    """

    request = 'champion/{name}/general'.format(name=champion)
    return [PyGGObject(datum) for datum in pygg.requests.get(request)]


def get_champion_matchups(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMatchups
    """

    request = '/champion/{name}/matchup'.format(name=champion)
    return [PyGGObject(datum) for datum in pygg.requests.get(request)]


def get_most_popular_items(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostPopularItems
    """

    request = '/champion/{name}/items/finished/mostPopular'.format(name=champion)
    return [PyGGObject(datum) for datum in pygg.requests.get(request)]


def get_most_popular_skills(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostPopularSkill
    """

    request = '/champion/{name}/skills/mostPopular'.format(name=champion)
    return [PyGGObject(datum) for datum in pygg.requests.get(request)]


def get_most_popular_starter_items(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostPopularStartingItems
    """

    request = '/champion/{name}/items/starters/mostPopular'.format(name=champion)
    return [PyGGObject(datum) for datum in pygg.requests.get(request)]


def get_most_popular_summoners(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostPopularSummoners
    """

    request = '/champion/{name}/summoners/mostPopular'.format(name=champion)
    return [PyGGObject(datum) for datum in pygg.requests.get(request)]


def get_most_winning_items(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostWinningItems
    """

    request = '/champion/{name}/items/finished/mostWins'.format(name=champion)
    return [PyGGObject(datum) for datum in pygg.requests.get(request)]


def get_most_winning_starter_items(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostWinningStartingItems
    """

    request = '/champion/{name}/items/starters/mostWins'.format(name=champion)
    return [PyGGObject(datum) for datum in pygg.requests.get(request)]


def get_most_winning_summoners(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostWinningSummoners
    """

    request = '/champion/{name}/summoners/mostWins'.format(name=champion)
    return [PyGGObject(datum) for datum in pygg.requests.get(request)]


def get_most_popular_runes(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostPopularRunes
    """

    request = '/champion/{name}/runes/mostPopular'.format(name=champion)
    return [PyGGObject(datum) for datum in pygg.requests.get(request)]


def get_most_winning_runes(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostWinningRunes
    """

    request = '/champion/{name}/runes/mostWins'.format(name=champion)
    return [PyGGObject(datum) for datum in pygg.requests.get(request)]


def get_most_winning_skills(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionMostWinningSkill
    """

    request = '/champion/{name}/skills/mostWins'.format(name=champion)
    return [PyGGObject(datum) for datum in pygg.requests.get(request)]


def get_skills(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionSkills
    """

    request = '/champion/{name}/skills'.format(name=champion)
    return [PyGGObject(datum) for datum in pygg.requests.get(request)]


def get_skills(champion):
    """champion    <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionSkills
    """

    request = '/champion/{name}/skills'.format(name=champion)
    return [PyGGObject(datum) for datum in pygg.requests.get(request)]


def get_skills(champion):
    """champion    <str> champion name
    enemy       <str> champion name
    return      http://api.champion.gg/docs/#api-Champion-GetChampionSpecificMatchup
    """

    request = '/champion/{name}/matchup/{enemy}'.format(name=champion, enemy=enemy)
    return [PyGGObject(datum) for datum in pygg.requests.get(request)]
