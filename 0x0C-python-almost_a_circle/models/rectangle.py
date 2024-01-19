#!/usr/bin/python3
"""Module for the first rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A rectangle class that inherits from the
    base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiate constructor"""

        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if not isinstance(x, int):
            raise TypeError("x must be an integer")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        if height <= 0:
            raise ValueError("height must be > 0")

        if x < 0:
            raise ValueError("x must be >= 0")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """method to retrieve the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Method to change the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Method to retrieve the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Method to change the value of height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Method to retrieve the value of x"""

        return self.__x

    @x.setter
    def x(self, value):
        """Method to change the value of x"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Method to retrieve the value of y"""

        return self.__y

    @y.setter
    def y(self, value):
        """Method to change the value of y"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Method to retrieve the area of rectangle"""

        return self.height * self.width

    def display(self):
        """Method to display the size of the rectangle"""
        print("\n" * self.y, end='')
        for x in range(self.height):
            print((" " * self.x) + ("#" * self.width))

    def __str__(self):
        """Method to overwrite the actual output for str"""

        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} "
                f"- {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """Method to update values from unknown variable count"""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Method to return the dict format"""

        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
