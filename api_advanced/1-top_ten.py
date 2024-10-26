#!/usr/bin/python3
"""
This script prints the titles of the first 10 hot posts for a given subreddit.
If the subreddit does not exist or cannot be accessed, it prints "OK" as required.
"""

import requests


def top_ten(subreddit):
    """Fetches and prints the top 10 hot post titles for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyRedditClient/0.1"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json().get("data", {})
            hot_posts = data.get("children", [])
            
            # Print titles if hot posts exist, else print None
            if hot_posts:
                for post in hot_posts:
                    print(post["data"].get("title"))
            else:
                print(None)
        else:
            # Output "OK" for non-existent subreddits
            print("OK")
    except requests.exceptions.RequestException:
        print("OK")  # Print "OK" on network errors as well
