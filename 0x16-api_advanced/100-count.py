#!/usr/bin/python3
"""Reddit API - Count occurrences of specified words in hot posts."""

import requests
import re
from collections import defaultdict


def count_words(subreddit, word_list, after="", counts=None):
    """
    Recursively queries the Reddit API 
    and counts the occurrences of keywords in hot post titles.
    """
    if counts is None:
        counts = defaultdict(int)

    user_agent = {'User-Agent': 'api_advanced-project'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after}

    try:
        response = requests.get(url, headers=user_agent,
                                params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            after = data.get('after')
            posts = data.get('children', [])

            # Extract and process titles
            for post in posts:
                title = post['data']['title'].lower()
                words = re.findall(r'\b\w+\b', title)

                for word in words:
                    if word in map(str.lower, word_list):
                        counts[word] += 1

            # If there's more data to fetch, recurse
            if after:
                return count_words(subreddit, word_list, after, counts)

            # Process and print results
            sorted_counts = sorted(counts.items(),
                                   key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")

        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None
