#!/usr/bin/python3
def uppercase(str):
    new = ''
    for x in str:
        if ord(x) >= 97 and ord(x) <= 123:
            new += chr(ord(x) - 32)
        else:
            new += x
    print('{}'.format(new))
