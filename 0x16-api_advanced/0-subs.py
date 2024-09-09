#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests

def number_of_subscribers(subreddit):
    """ 
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function returns 0.
    
    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        int: Number of subscribers to the subreddit, or 0 if the subreddit is invalid.
    """
    headers = {'User-Agent': 'custom_user_agent'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
    
    except Exception:
        return 0
    
    return 0
