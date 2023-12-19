#!/usr/bin/python3
class Square:
    """A class to define a square"""
    def __init__(self, size=0):
        """a method to instantiate a private instance attribute"""
        if isinstance(size, int):
            self.__self = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
