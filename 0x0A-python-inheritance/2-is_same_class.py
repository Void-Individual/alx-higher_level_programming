#!/usr/bin/python3
"""Module to test true or false for an object"""


def is_same_class(obj, a_class):
    """Function to compare an the type of an
     object to another class"""

    da_ty = type(obj)

    if da_ty is a_class:
        return True
    else:
        return False
