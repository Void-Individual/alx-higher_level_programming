#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter
as a parameter."""

import requests
from sys import argv

if __name__ == "__main__":
    if argv[1]:
        letter = argv[1]
    else:
        letter = ""
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}

    response = requests.post(url, data)
    try:
        result = response.json()
        if result:
            print("[{}] {}".format(result['id'], result['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
