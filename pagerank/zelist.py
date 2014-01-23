import httplib
import re
import urllib2
import urlparse

__author__ = 'valibanu'

from rank_provider import RankProvider


class ZelistRank(RankProvider):
    def __init__(self, host="zelist.ro", proxy=None, timeout=30):
        """
        Get the Zelist rank for sites enrolled in the service
        @param host: toolbar host address
        @param proxy: address of proxy server (if required). Default: None
        @param timeout: how long to wait for a response from the server.
        Default: 30 (seconds)
        """
        super(ZelistRank, self).__init__(host, proxy, timeout)
        self._regex = re.compile("Pozitia in clasament:\s+(\d+)")

    def get_rank(self, page):
        """
        Return the Zelist rank of an enrolled site
        @rtype : object
        @param page: short string of the URL (eg. nwradu.ro)
        """
        query = 'http://{0}/bloguri/{1}'.format(self._host,
                                                urllib2.quote(page, safe=''))
        response = self._opener.open(query, timeout=self._timeout)
        if response.getcode() == httplib.OK:
            data = response.read()
            match = re.search(r'Pozitia in clasament:\s+(\d+)', data)
            if match:
                return int(match.group(1))
            else:
                return 0


def get_zelist_rank(url):
    """
    Return the Zelist Rank of a given page
    @rtype : object
    @param url: full string of the URL (eg. http://www.nwradu.ro)
    """
    # get short URL name
    page = urlparse.urlparse(url).hostname
    if 'www' in page:
        page = page[4:]
    return ZelistRank().get_rank(page)
