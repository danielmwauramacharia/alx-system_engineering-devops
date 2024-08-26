#!/usr/bin/python3
"""
Using Reddit's API to retrieve titles of all hot posts for a subreddit recursively.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, returns None.
    """
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after}

    try:
        results = requests.get(
            url, params=params, headers=user_agent, allow_redirects=False)

        if results.status_code == 200:
            data = results.json().get("data", {})
            after = data.get("after")
            all_titles = data.get("children", [])

            # Append titles to hot_list
            for title_ in all_titles:
                hot_list.append(title_.get("data", {}).get("title"))

            # If there's more data to fetch, continue the recursion
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list if hot_list else None
        else:
            return None
    except Exception:
        return None
