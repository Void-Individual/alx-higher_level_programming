#!/usr/bin/python3
def uniq_add(my_list=[]):
    temp = []
    sum = 0
    cnt = len(my_list)
    for x in range(cnt):
        num = my_list[x]
        for y in temp:
            if num == y:
                num -= 1
                break
        if num != my_list[x]:
            continue
        temp.append(num)
        sum += num
    return sum
