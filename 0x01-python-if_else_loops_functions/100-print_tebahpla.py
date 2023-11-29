#!/usr/bin/python3
for x in range(25, -1, -2):
    print('{}{}'.format(chr(97 + x),chr(65 + (x - 1))), end='')
