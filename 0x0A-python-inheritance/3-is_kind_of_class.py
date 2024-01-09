#!/usr/bin/python3
"""Module to check an objects instance"""


def is_kind_of_class(obj, a_class):
    """Method to test if obj is an instance of a class,
     or the instance of one of it sub-classes"""

    return isinstance(obj, a_class)
