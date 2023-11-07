#!/usr/bin/python3
""""Doc"""
import requests


def number_of_subscribers(subreddit):
    subreddit = "programming"
    headers = {
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
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

# subreddit = "programming"
# sub_count = number_of_subscribers(subreddit)
# if sub_count is not None:
#     print(f"The subreddit r/{subreddit} has {sub_count} subscribers.")
