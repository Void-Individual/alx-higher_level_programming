#!/usr/bin/python3
"""Module to append text to a file"""


def append_write(filename="", text=""):
    """Function to append txt to a file"""

    with open(filename, 'a') as file:
        count = file.write(text)

    return count
