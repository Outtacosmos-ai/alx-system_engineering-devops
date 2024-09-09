#!/usr/bin/python3
"""
file for top_ten method
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the top ten hot posts
    of a given subreddit.
    If an invalid subreddit is given, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for i in range(min(10, len(children))):
                print(children[i].get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")
