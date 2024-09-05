#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.
    If the subreddit is invalid, return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"  # Custom User-Agent
    }

    try:
        # Request subreddit data
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response status code is not 200 (OK)
        if response.status_code != 200:
            return 0

        # Parse the JSON response
        data = response.json().get("data")

        # Return the number of subscribers if data exists, otherwise return 0
        return data.get("subscribers", 0) if data else 0

    except Exception:
        # Catch any errors (like network issues) and return 0
        return 0
