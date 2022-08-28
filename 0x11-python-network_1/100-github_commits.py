#!/usr/bin/python3
"""
List 10 commits (from the most recent to oldest) of the repository “rails”
by the user “rails”. You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/. Print all commits by:
`<sha>: <author name>` (one by line)

Python script that takes 2 arguments in order to solve this challenge:
"""

import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    user = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(user, repo)

    resp = requests.get(url).json()

    for c in resp[:10]:
        print(c.get("sha") + ": " + c.get("commit").get("author").get("name"))
