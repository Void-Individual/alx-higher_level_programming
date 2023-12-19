#!/usr/bin/python3
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
