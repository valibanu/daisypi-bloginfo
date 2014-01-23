import os
from pagerank.alexa import get_alexa_traffic_rank
from pagerank.facebook import get_facebook_info
from pagerank.google import get_google_page_rank
from pagerank.twitter import get_twitter_info
from pagerank.zelist import get_zelist_rank

__author__ = 'valibanu'


DEBUG = True if 'DEBUG' in os.environ else False


def get_first_row(alexa_rank, google_rank, zelist_rank):
    """
    Print the first line of the 2 X 16 LCD with in formation about the Alexa
    rank, Google page rank and Zelist rank
    @param alexa_rank: data to be printed
    @param google_rank: data to be printed
    @param zelist_rank: data to be printed
    @return: the string of characters
    """
    prefix = ':'
    if zelist_rank:
        figures = len('{}{}{}'.format(alexa_rank, google_rank, zelist_rank))
        if figures > 8:
            prefix = ''
        separator = ((16 - figures - 3 * (len(prefix) + 1)) / 2) * ' '
        return 'A{0}{1}{2}G{0}{3}{2}Z{0}{4}'.format(prefix, alexa_rank,
                                                    separator, google_rank,
                                                    zelist_rank)
    else:
        figures = len('{}{}'.format(alexa_rank, google_rank))
        if figures > 11:
            prefix = ''
        separator = ((16 - figures - 2 * (len(prefix) + 1) - 1) / 3) * ' '
        return '{0}A{1}{2} {0}G{1}{3}{0}'.format(separator, prefix,
                                                 alexa_rank, google_rank)


def get_second_row(twitter_info, facebook_info):
    """
    Print the second line of the 2 X 16 LCD with information about the
    Twitter followers and Facebook page likes.
    @param twitter_info: data to be printed
    @param facebook_info: data to be printed
    @return: the string of characters
    """
    figures = len('{}{}'.format(twitter_info, facebook_info))
    twitter_prefix = 'TW:'
    facebook_prefix = 'FB:'
    if figures > 9:
        if figures > 11:
            twitter_prefix = 'T'
            facebook_prefix = 'F'
        else:
            twitter_prefix = 'T:'
            facebook_prefix = 'F:'
    separator = ((16 - figures - len(twitter_prefix) - len(facebook_prefix) -
                  1) / 3) * ' '
    return '{0}{1}{2} {0}{3}{4}{0}'.format(separator, twitter_prefix,
                                           twitter_info, facebook_prefix,
                                           facebook_info)


def main():
    """
    Print the social media data in 2 X 16 characters format.
    (To be printed out on a 2 X 16 Serial LCD)
    """
    with open('config.txt') as conf_file:
        lines = conf_file.readlines()

        url = lines[0].split()[-1]
        twitter_id = lines[1].split()[-1]
        fb_page = lines[2].split()[-1]

        alexa_rank = get_alexa_traffic_rank(url)
        google_rank = get_google_page_rank(url)
        zelist_rank = get_zelist_rank(url)
        twitter_info = get_twitter_info(twitter_id)
        facebook_info = get_facebook_info(fb_page)

        if DEBUG:
            print(url)
            print('Alexa Traffic Rank: {}'.format(alexa_rank))
            print('Google Page Rank: {}'.format(google_rank))
            if zelist_rank:
                print('Zelist Rank: {}'.format(zelist_rank))
            else:
                print('Blog "{}" not present in Zelist!'.format(url))
            #TODO: Better error handling
            if twitter_info >= 0:
                print('Twitter followers: {}'.format(twitter_info))
            else:
                print('Error reading Twitter followers!')
            if facebook_info >= 0:
                print('Facebook Likes: {}'.format(facebook_info))
            else:
                print('Error reading Facebook likes!')
        else:
            #TODO: Better error handling
            print(get_first_row(alexa_rank, google_rank, zelist_rank))
            print(get_second_row(twitter_info, facebook_info))


if __name__ == '__main__':
    main()