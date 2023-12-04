#!/usr/bin/python3
a = 89
b = 10
a, b = __import__('switch-12').switch(a, b)
print("a={:d} - b={:d}".format(a, b))
