import httplib
import re
import urllib2


__author__ = 'valibanu'


def get_twitter_info(twitter_id):
    """
    Return the number of followers of a Twitter account
    @param twitter_id: Twitter handler
    """
    query = 'https://twitter.com/{}'.format(twitter_id)
    response = urllib2.build_opener().open(query, timeout=10)
    if response.getcode() == httplib.OK:
        data = response.read()
        return int(re.search(r'&quot;followers_count&quot;:('r'\d+)',
                             str(data)).group(1))
    else:
        return -1
