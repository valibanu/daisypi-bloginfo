import httplib
import re
import urllib2

from BeautifulSoup import BeautifulSoup

__author__ = 'valibanu'


def get_twitter_info(twitter_id):
    """
    Print the number of followers of a Twitter account
    @param twitter_id: Twitter handler
    """
    query = 'https://twitter.com/{}'.format(twitter_id)
    response = urllib2.build_opener().open(query, timeout=10)
    if response.getcode() == httplib.OK:
        data = response.read()
        soup = BeautifulSoup(data)
        print('Twitter followers: {}'.format(re.search(r'"followers_count":('
                                                       r'\d+)',
                                                       str(soup)).group(1)))
