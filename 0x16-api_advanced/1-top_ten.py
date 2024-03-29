#!/usr/bin/python3
"""Function that queries the Reddit API and
prints the titles of the first 10 hot posts listed"""
import requests


def top_ten(subreddit):
    """Function that queries the Reddit API and
    prints the titles of the first 10 hot posts listed"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        for i in range(10):
            print(response.json().get('data').
                  get('children')[i].get('data').get('title'))
    else:
        print('None')
