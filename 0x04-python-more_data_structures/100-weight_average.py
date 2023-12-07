#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    count = len(my_list)
    nume = 0
    denom = 0
    for x in range(count):
        tup = my_list[x]
        nume += tup[0] * tup[1]
        denom += tup[1]
    total = nume / denom
    return total
