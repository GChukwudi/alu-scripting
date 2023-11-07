#!/usr/bin/python3
""""
Doc
"""


import requests


def number_of_subscribers(subreddit):
    subreddit = "programming"
    headers = {
        "User_Agent": "Mozilla/5.0"
    }
    URL = f"https://www.reddit.com/r/{subreddit}/about.json"

    raw_response = requests.get(URL, headers=headers)

    if raw_response.status_code == 200:
        json_response = raw_response.json()
        sub_count = json_response['data']['subscribers']
        return sub_count
    else:
        # Handle the case where the subreddit is invalid or another error occurred
        print(f"Error: Could not retrieve data for subreddit '{subreddit}'. Status code: {raw_response.status_code}")
        return None
