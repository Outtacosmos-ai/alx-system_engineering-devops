#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function returns 0.
    """
    # Define the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set up a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'custom_user_agent'}
    
    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful and contains the correct data
    if response.status_code == 200:
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    
    # If not successful, return 0
    return 0
