#!/usr/bin/python3
"""" Top Ten Limit"""
import requests


def top_ten(subreddit):
    """"top ten"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)