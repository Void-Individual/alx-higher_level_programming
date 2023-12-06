#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cnt = len(my_list)
    new = []
    for x in range(cnt):
        if my_list[x] == search:
            new.append(replace)
        else:
            new.append(my_list[x])
    return new
