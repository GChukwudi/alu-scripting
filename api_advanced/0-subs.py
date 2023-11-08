#!/usr/bin/python3
""""
returns the number of subscribers (not active users,
total subscribers)for a givensubreddit. If an 
invalid subreddit is given, the function should return 0
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    # subreddit = "programming"
    URL = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    my_headers = {
        "User-Agent": "myApp 0.1 (by /u/favour_DC)"
        }
    
    raw_response = requests.get(URL, headers=my_headers, allow_redirects=False)
        
    if raw_response.status_code == 200:
        json_response = raw_response.json()
        sub_count = json_response['data']['subscribers']
        return sub_count
                
    else: 
        return 0
