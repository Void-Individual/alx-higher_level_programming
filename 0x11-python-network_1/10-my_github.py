#!/usr/bin/python3
"""Write a Python script that takes your GitHub credentials (username
and password) and uses the GitHub API to display your id"""

import requests
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    pwd = argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, pwd))
    if response.status_code == 200:
        info = response.json()
        print(info.get("id"))
    else:
        print("None")
