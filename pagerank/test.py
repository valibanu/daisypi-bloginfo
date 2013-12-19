from pagerank.facebook import get_facebook_info

__author__ = 'valibanu'


def test_func():
    """
    test calls.

    @rtype : object
    """
    # b1 = 'http://www.zoso.ro'
    # get_google_page_rank(b1)
    # get_alexa_traffic_rank(b1)
    # get_zelist_rank(b1)
    #
    # b2 = 'http://www.nwradu.ro'
    # get_google_page_rank(b2)
    # get_alexa_traffic_rank(b2)
    # get_zelist_rank(b2)

    # get_twitter_info('valibanu')
    get_facebook_info('https://www.facebook.com/pages/RoboFun/130284110395666')
    get_facebook_info('https://www.facebook.com/nwradu.ro')
