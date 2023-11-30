#!/usr/bin/python3
for x in range(26):
    if x != 25:
        print('{}'.format(chr(65 + x)), end='')
    else:
        print('{}'.format(chr(65 + x)))
