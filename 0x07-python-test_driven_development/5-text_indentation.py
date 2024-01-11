#!/usr/bin/python3
"""Module do edit str"""


def text_indentation(text):
    """FUnction to print a text with 2
    new lines after specific characters"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    check = 0
    for chr in text:
        if ((chr == '.') or (chr == '?')
            or (chr == ':')):
            print('\n')
            check += 1
        else:
            if check and chr == ' ':
                check -= 1
                continue
            print(chr, end='')
