#!/usr/bin/python3
"""Module square inherits from rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square subclass"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        return super().area()

    def __str__(self):
        return f"[square] {self.__size}/{self.__size}"
