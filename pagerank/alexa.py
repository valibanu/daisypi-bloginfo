from rank_provider import AlexaTrafficRank

__author__ = 'valibanu'


def get_alexa_traffic_rank(url):
    """
    Return Alexa Rank for a given URL
    @param url: full string of the URL (eg. http://www.google.ro)
    """
    return AlexaTrafficRank().get_rank(url)
