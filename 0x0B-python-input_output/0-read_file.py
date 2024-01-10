#!/usr/bin/python3
"""Module to read a text and print to stdout"""


def read_file(filename=""):
    """FUnction to open a file"""

    with open(filename, 'r') as file:
        print(file.read())
