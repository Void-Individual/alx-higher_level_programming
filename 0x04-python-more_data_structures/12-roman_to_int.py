#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or roman_string.isdigit():
        return 0
    nume = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    count = len(roman_string)
    sum = 0
    for st in range(count):
        key = roman_string[st]
        sum += nume[key]
    return sum
