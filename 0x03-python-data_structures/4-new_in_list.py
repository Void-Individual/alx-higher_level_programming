#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    count = len(my_list)
    if idx > count:
        return my_list
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
