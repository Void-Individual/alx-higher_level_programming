#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    count = len(my_list)
    new_list = [0] * count
    for x in range(count):
        if my_list[x] % 2 != 0:
            new_list[x] = 0
        else:
            new_list[x] = 1

    return new_list
