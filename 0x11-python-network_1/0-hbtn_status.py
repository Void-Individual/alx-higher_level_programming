#!/usr/bin/python3
"""A script that fetches a url"""

from urllib import request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        content = response.read()
    content_str = content.decode('utf-8')
    print("Body response:")
    print("\t- type: ", type(content))
    print("\t- content: ", content)
    print("\t- utf8 content: ", content_str)
