#!/usr/bin/python3
""""Module"""
import requests


def number_of_subscribers(subreddit):
        subreddit = "programming"
        URL = f"https://www.reddit.com/r/{subreddit}/about.json"

        my_headers = {
            "User-Agent": "Chrome 0.2 (by /u/favour_DC)"
        }

        raw_response = requests.get(URL, headers=my_headers, allow_redirects=False)
        
        if raw_response.status_code == 200:
            json_response = raw_response.json()
            sub_count = json_response['data']['subscribers']
            print(sub_count)
                
        else: 
            print("Invalid Subreddit")

number_of_subscribers('programming')
