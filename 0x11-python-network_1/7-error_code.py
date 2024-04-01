#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the
URL and displays the body of the response."""

from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    print(response.text)
