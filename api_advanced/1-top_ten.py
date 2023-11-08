#!/usr/bin/python3
"""" Top Ten Limit"""
import requests


def top_ten(subreddit):
    """"top ten"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    my_headers = {
        "User-Agent": "myApp 0.1 (by /u/favour_DC)"
        }

    response = requests.get(URL, headers=my_headers)
    raw_response = response.json()['data']['children']

    if raw_response.status_code == 200:
        json_response = raw_response.json()
        post = json_response['data']['subscribers']
        return post

    else:
        return 0
