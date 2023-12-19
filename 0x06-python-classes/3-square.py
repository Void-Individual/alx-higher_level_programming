#!/usr/bin/python3
class Square:
    """A class to define a square"""
    def __init__(self, size=0):
        """Instantialization of private instance variable"""
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Method to output the area of square"""
        return self.__size ** 2
