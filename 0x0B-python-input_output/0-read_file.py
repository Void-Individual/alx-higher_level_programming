#!/usr/bin/python3
"""Module to read a text and print to stdout"""


def read_file(filename=""):
    """Function to open a file"""

    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end='')
