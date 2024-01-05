#!/usr/bin/python3
"""This is a module for the rectangle class"""


class Rectangle:
    """This class will def height and width"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation of the class"""

        if isinstance(width, int):
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
        Rectangle.number_of_instances += 1

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
        if self.__height == 0 or self.__width == 0:
            return rect
        self.print_symbol = str(self.print_symbol)

        while count_height <= self.__height:
            if count_height != self.__height:
                rect += self.print_symbol * self.__width + "\n"
            if count_height == self.__height:
                rect += self.print_symbol * self.__width
            count_height += 1

        return rect

    def __repr__(self):
        """Method to return new instance representation"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Method to delete an instance"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method to compare 2 instances"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            rect_2

    @classmethod
    def square(cls, size=0):
        """Method to form a square"""

        return cls(size, size)
