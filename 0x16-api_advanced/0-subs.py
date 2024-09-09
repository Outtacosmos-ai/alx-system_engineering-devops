#!/usr/bin/python3
"""
Module to query the Reddit API and get the number of subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:v1:subscriberbot"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    return 0
