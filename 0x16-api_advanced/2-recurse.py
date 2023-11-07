#!/usr/bin/python3
"""Function that queries the Reddit API and
returns a list containing the titles of all hot articles"""
import requests


def recurse(subreddit, hot_list=[]):
    """Function that queries the Reddit API and
    returns a list containing the titles of all hot articles"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        for i in range(10):
            hot_list.append(response.json().get('data').
                            get('children')[i].get('data').get('title'))
        return recurse(subreddit, hot_list)
    else:
        return hot_list
