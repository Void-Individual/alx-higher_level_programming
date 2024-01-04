#!/usr/bin/python3
"""This is a module for the rectangle class"""


class Rectangle:
    """This class will def height and width"""

    def __init__(self, width=0, height=0):
        """Instantiation of the class"""

        if isinstance(height, int):
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

        if isinstance(width, int):
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Method to retrieve height value"""

        return self.__height

    @height.setter
    def height(self, value):
        """Method to change height value"""

        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """Method to retrieve width value"""

        return self.__width

    @width.setter
    def width(self, value):
        """Method to change width value"""

        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    def area(self):
        """Method to derive the area of values"""

        return self.__height * self.__width

    def perimeter(self):
        """Method to derive the perimeter of values"""

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Method to return output to str format #"""

        count_height = 1
        rect = ""
        while count_height <= self.__height:
            if count_height != self.__height:
                rect += "#" * self.__width + "\n"
            if count_height == self.__height:
                rect += "#" * self.__width
            count_height += 1

        return rect

    def __repr__(self):
        """Method to return new instance representation"""

        return f"Rectangle({self.__width}, {self.__height})"
