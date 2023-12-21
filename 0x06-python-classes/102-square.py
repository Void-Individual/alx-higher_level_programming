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
            raise TypeError("size must be a number")

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
            raise TypeError("size must be a number")

    def area(self):
        """Method to to retrieve the area"""
        return self.__size ** 2

    def __lt__(self, other):
        """Method to check for less than"""
        return self.area() < other.area()

    def __le__(self, other):
        """Method to check for less than or equal to"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Method to check for greater than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Method to check for greater than or equal to"""
        return self.area() >= other.area()

    def __eq__(self, other):
        """Method to check for equal to"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Method to check for not equal to"""
        return self.area() != other.area()
