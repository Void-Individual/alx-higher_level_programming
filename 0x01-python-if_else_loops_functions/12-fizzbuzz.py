#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0:
            print('Fizz', end='')
        if x % 5 == 0:
            print('Buzz', end='')
        if x % 3 != 0 and x % 5 != 0:
            print(x, end='')
        if x != 100:
            print(' ', end='')
        elif x == 100:
            print('', end='')
