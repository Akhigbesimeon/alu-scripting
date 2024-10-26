#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Main function"""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    HEADERS = {"User-Agent": "MyRedditClient/0.1"}
    
    try:
        response = requests.get(URL, headers=HEADERS, allow_redirects=False)
        
        # Check if status is OK
        if response.status_code == 200:
            data = response.json().get("data")
            if data:
                hot_posts = data.get("children", [])
                
                # Check if hot_posts is populated
                if hot_posts:
                    for post in hot_posts:
                        print(post["data"].get("title"))
                else:
                    print("No hot posts found.")
            else:
                print("OK")  # Non-existent subreddit case
        else:
            print("OK")  # Non-existent subreddit case
    except requests.exceptions.RequestException:
        print("OK")  # Network error or request failure
