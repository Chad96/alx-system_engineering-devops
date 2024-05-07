#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "MyRedditBot"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data["data"]["subscribers"]
    except (requests.RequestException, KeyError):
        # Handle invalid subreddit or other errors
        return 0


if __name__ == "__main__":
    subreddit_name = input("Enter the subreddit name: ")
    subscribers_count = number_of_subscribers(subreddit_name)
    print(f"Subscribers in r/{subreddit_name}: {subscribers_count}")
