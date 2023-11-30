#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    count = len(argv)
    if count == 1:
        print('0')
    else:
        plus = 0
        for x in range(1, count):
            plus += int(argv[x])

        print('{}'.format(plus))
