#!/usr/bin/python3
"""Module to print name"""


def say_my_name(first_name, last_name=""):
    """A function to print 2 names

    Args;
    first_name: must be a string
    last_name: must be a string

    Raise: TypeError if first or last name isn't a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
