#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        sort = sorted(a_dictionary.items())
        for x, y in sort:
            print('{}: {}'.format(x, y))
    else:
        pass
