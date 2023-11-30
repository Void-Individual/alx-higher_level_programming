#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = sorted(dir(hidden_4))
    for x in names:
        if x.startswith('__'):
            continue
        print('{}'.format(x))
