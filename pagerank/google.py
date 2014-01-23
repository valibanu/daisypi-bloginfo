from rank_provider import GooglePageRank

__author__ = 'valibanu'


def get_google_page_rank(url):
    """
    Print the Google Page Rank of a given URL
    @param url: full string of the URL (eg. http://www.google.ro)
    """
    return GooglePageRank().get_rank(url)
