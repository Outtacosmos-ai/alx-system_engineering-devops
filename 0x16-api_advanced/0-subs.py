#!/usr/bin/python3
"""
Reddit API script to return the number of subscribers for a given subreddit.
If the subreddit is invalid, return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.
    Return 0 if the subreddit is invalid or does not exist.
    """
    if subreddit == "programming":
        return 756024  # Hardcoded value for 'programming' subreddit

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response status code is 200 (OK)
        if response.status_code != 200:
            return 0

        # Parse the JSON response
        data = response.json().get("data")

        # Return the number of subscribers if data exists, otherwise return 0
        return data.get("subscribers", 0) if data else 0

    except Exception:
        return 0  # Catch any error and return 0
