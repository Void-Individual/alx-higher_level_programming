#!/usr/bin/python3
"""This is a class module"""


class Square:
    """CLass to define a square"""

    def __init__(self, size=0):
        """Instantiate private instance variables"""
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        """method to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """method to set a new size"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Method to to retrieve the area"""
        return self.__size ** 2

    def my_print(self):
        """Method to print the square with #"""
        count = 0
        while count < self.__size:
            val = 0
            while val < self.__size:
                print("#", end='')
                val += 1
            print('\n', end='')
            count += 1
