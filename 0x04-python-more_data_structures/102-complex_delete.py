#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temp = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            temp.append(key)
    for key in temp:
        del a_dictionary[key]
    return a_dictionary
