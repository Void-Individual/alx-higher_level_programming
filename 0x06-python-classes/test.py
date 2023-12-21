#!/usr/bin/python3
magic_module = __import__('103-magic_class')

# Creating an instance of MagicClass with a radius of 10
mc = magic_module.MagicClass(10)

print("{:.2f}".format(mc.area()))
