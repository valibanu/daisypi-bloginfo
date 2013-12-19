from rank_provider import AlexaTrafficRank

__author__ = 'valibanu'


def get_alexa_traffic_rank(url):
    """
    Print Alexa Rank for a given URL
    @param url: full string of the URL (eg. http://www.google.ro)
    """
    print('Alexa Traffic Rank: {}'.format(AlexaTrafficRank().get_rank(url)))
