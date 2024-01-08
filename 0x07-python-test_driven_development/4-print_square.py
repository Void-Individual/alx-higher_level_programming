#!/usr/bin/python3
"""Module to print #"""


def print_square(size):
    """A function to print a square with the char #

    Args;
    size: the length and breadth of the square

    Raise:
    - TypeError if size is not an integer
    - ValuError if size < 0
    """

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        if isinstance(size, int):
            raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    size = int(size)
    for x in range(size):
        print("#" * size)
