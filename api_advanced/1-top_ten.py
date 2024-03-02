import requests

def top_ten(subreddit):
    url = "https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
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

# Example usage:
# top_ten("programming")

