#!/usr/bin/python3
"""
Prints the titles of the first 10
hot posts listed for a given subreddit.
"""

from requests import get


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit. If the subreddit
    is invalid, prints None.
    """
    if not isinstance(subreddit, str) or subreddit is None:
        print("None")
        return

    user_agent = {'User-Agent': 'api_advanced-project'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    try:
        response = get(url, headers=user_agent,
                       params=params, allow_redirects=False)

        if response.status_code == 200:
            results = response.json()
            posts = results.get('data', {}).get('children', [])
            if posts:
                for post in posts:
                    print(post.get('data', {}).get('title', ""))
            else:
                print("None")
        else:
            print("None")
    except Exception:
        print("None")
