#!/usr/bin/python3
"""Module containing a function for peaks"""

def find_peak(list_of_integers):
    """Function to find and returrn the peak in a list of integers"""

    if not isinstance(list_of_integers, list):
        return None
    if len(list_of_integers) == 0:
        return None

    check = 0
    count = len(list_of_integers)
    for num in list_of_integers:
        for x in range(count):
            if num < list_of_integers[x]:
                check = 0
                break
            elif x == count - 1:
                check = 1
        if check:
            return num
