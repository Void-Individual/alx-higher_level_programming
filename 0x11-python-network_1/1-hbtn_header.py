#!/usr/bin/python3
"""A script to take in a url, send a request to it
and display a specific value"""

from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        id = response.headers.get('X-Request-Id')
        if id:
            print(id)
