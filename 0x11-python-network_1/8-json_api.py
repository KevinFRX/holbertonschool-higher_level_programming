#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    q = {"q": q}

    resp = requests.post(url, q)

    try:
        jason = resp.json()
        if jason == {}:
            print("No result")
        else:
            print("[{}] {}".format(jason.get("id"), jason.get("name")))
    except:
        print("Not a valid JSON")
