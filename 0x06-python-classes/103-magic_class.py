#!/usr/bin/python3
"""A magic calculation module"""


class MagicClass:
    """A class to replicate bytecode"""
    def __init__(self, radius):
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError("radius must be a number")
            self.__radius = radius

    def area(self):
        """Method to check for the area"""
        return (self.__radius ** 2) * (22 / 7)

    def circumference(self):
        """Method to check for the perimeter"""
        return (2 * (22 / 7)) * self.__radius
