#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    from sys import argv, exit

    count = len(argv)

    if count != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == '+':
        print('{} + {} = {}'.format(a, b, add(a, b)))
    elif argv[2] == '-':
        print('{} - {} = {}'.format(a, b, sub(a, b)))
    elif argv[2] == '/':
        print('{} / {} = {}'.format(a, b, div(a, b)))
    elif argv[2] == '*':
        print('{} * {} = {}'.format(a, b, mul(a, b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
