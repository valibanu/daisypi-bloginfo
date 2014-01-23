import httplib
import re
import urllib2

__author__ = 'valibanu'


def get_facebook_info(fb_page):
    """
    Return the number of likes of a Facebook page
    @param fb_page: full string of the URL
    (eg. https://www.facebook.com/nwradu.ro)
    """
    query = ('https://api.facebook.com/method/fql'
             '.query?query=select%20like_count%20from%20link_stat%20where%20'
             'url=%27{}/%27&format=json'.format(fb_page))
    response = urllib2.build_opener().open(query, timeout=10)
    if response.getcode() == httplib.OK:
        data = response.read()
        return int(re.search(r'\d+', str(data)).group(0))
    else:
        return -1
