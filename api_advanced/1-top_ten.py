#!/usr/bin/python3
"""
<<<<<<< HEAD
This module contains a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""

=======
This module contains a function that queries the Reddit API and
 returns the number of subscribers for a given subreddit.
"""
>>>>>>> e18c29d0f284b623f5143ba028641dd8f9447d23
import requests

def top_ten(subreddit):
    """
    Function to retrieve and print the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to search.

    Returns:
        None
    """
    url = "https://www.reddit.com/dev/api/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if not posts:
            print("No posts found.")
        else:
            for post in posts:
                print(post['data']['title'])
    else:
        print("None")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

