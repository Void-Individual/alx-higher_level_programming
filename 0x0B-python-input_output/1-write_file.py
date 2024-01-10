#!/usr/bin/python3
"""Module to write to a file"""


def write_file(filename="", text=""):
    """Function to write to a file"""

    with open(filename, 'w') as opened_file:
        count = opened_file.write(text)

    return count
