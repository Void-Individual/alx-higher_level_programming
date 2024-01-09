#!/usr/bin/python3
"""Module to check an objects instance"""


def inherits_from(obj, a_class):
    """Method to test if obj is an instance of a class,
     or for one of its subclasses"""

    da_ty = type(obj)
    if da_ty is a_class:
        return False

    return isinstance(obj, a_class)
