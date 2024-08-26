#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers to the subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My-User-Agent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
    except requests.RequestException:
        pass

    return 0
