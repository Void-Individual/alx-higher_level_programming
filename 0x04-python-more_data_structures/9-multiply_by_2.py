#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    sort = a_dictionary.items()
    new = {}
    for x, y in sort:
        new[x] = y * 2
    return new
