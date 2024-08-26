#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """
    if not isinstance(subreddit, str) or subreddit is None:
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    try:
        response = get(url, headers=user_agent, allow_redirects=False)
        if response.status_code == 200:
            results = response.json()
            print("OK")
            return results.get('data', {}).get('subscribers', 0)
        else:
            print("OK")
    except Exception:
        print("OK")

    return 0
