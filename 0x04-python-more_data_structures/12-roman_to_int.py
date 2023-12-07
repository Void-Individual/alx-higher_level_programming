#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or roman_string.isdigit():
        return 0

    nume = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    count = len(roman_string)
    sum = 0
    ls_rn = []
    for st in range(count):
        key = roman_string[st]
        ls_rn.append(nume[key])

    count = len(ls_rn)
    x = 0
    curr = 0
    last = 0
    while x < count:
        curr = ls_rn[x]
        if last != 0 and last < curr:
            sum = sum - last + (curr - last)
        else:
            sum += curr
        x += 1
        last = curr
    return sum
