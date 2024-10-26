#!/usr/bin/python3
"""
This script prints the titles of the first 10 hot posts for a given subreddit.
If the subreddit does not exist or cannot be accessed, it prints "OK" as required.
"""

import requests


def top_ten(subreddit):
    """Fetches and prints the top 10 hot post titles for a given subreddit"""
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
                print("OK")  # For non-existent subreddit case
        else:
            print("OK")  # For non-existent subreddit case
    except requests.exceptions.RequestException:
        print("OK")  # Network error or request failure

