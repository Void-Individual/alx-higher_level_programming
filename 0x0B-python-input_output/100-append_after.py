#!/usr/bin/python3
"""Module to modify file"""


def append_after(filename="", search_string="", new_string=""):
    """Function to add a new line of text after one
    that contains a specific string"""

    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
