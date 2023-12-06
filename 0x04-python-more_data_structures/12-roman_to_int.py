#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or roman_string.isdigit():
        return 0
    count = len(roman_string)
    sum = 0
    for st in range(count):
        num = roman_string[st]
        if num == 'X':
            sum += 10
    return sum
