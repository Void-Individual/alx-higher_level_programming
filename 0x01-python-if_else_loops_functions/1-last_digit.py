#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number >= 0:
    rem = number % 10
elif number < 0:
    rem = number % -10

if rem > 5:
    print(f'Last digit of {number:d} is {rem:d} and is greater than 5')
elif rem == 0:
    print(f'Last digit of {number:d} is {rem:d} and is 0')
else:
    print(f'Last digit of {number:d} is {rem:d} and is less than 6 and not 0')
