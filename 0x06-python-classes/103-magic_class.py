#!/usr/bin/python3
"""A magic calculation module"""

import math


class MagicClass:
    """A class to replicate bytecode"""
    def __init__(self, radius=0):
        if type(radius) not in (int, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Method to check for the area"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Method to check for the perimeter"""
        return (2 * math.pi) * self.__radius
