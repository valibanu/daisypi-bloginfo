from pagerank.alexa import get_alexa_traffic_rank
from pagerank.facebook import get_facebook_info
from pagerank.google import get_google_page_rank
from pagerank.twitter import get_twitter_info
from pagerank.zelist import get_zelist_rank

__author__ = 'valibanu'


if __name__ == '__main__':
    with open('config.txt') as conf_file:
        lines = conf_file.readlines()
        url = lines[0].split()[-1]
        twitter_id = lines[1].split()[-1]
        fb_page = lines[2].split()[-1]

        print(url)
        get_alexa_traffic_rank(url)
        get_google_page_rank(url)
        get_zelist_rank(url)
        get_twitter_info(twitter_id)
        get_facebook_info(fb_page)
