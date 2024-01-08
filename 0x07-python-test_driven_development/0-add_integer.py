#!/usr/bin/python3
"""
Module of a function to add 2 integers
"""


def add_integer(a, b=98):
    """Function to add 2 integers or floats
    a: First number
    b: Second number
    Returns the sum of the 2 numbers
    Raises TypeError if a and/or b aren't inteer or float numbers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
