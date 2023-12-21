#!/usr/bin/python3
"""This is a class module"""


class Square:
    """CLass to define a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiate private instance variables"""
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

        try:
            if (not isinstance(position[0], int) or
                    not isinstance(position[1], int)):
                raise TypeError("position must be a tuple"
                                "of 2 positive integer")
            else:
                if position[0] >= 0 and position[1] >= 0:
                    self.__position = position
                else:
                    raise TypeError("position must be a tuple"
                                    " of 2 positive integer")
        except Exception:
            raise Exception("position must be a tuple of 2 positive integer")

    @property
    def size(self):
        """method to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """private instance method to set a new size"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """private instance method to retrieve a position"""
        return self.__position

    @position.setter
    def position(self, value):
        """private instance method to set new position"""
        if (isinstance(value, tuple) and isinstance(value[0], int)
                and isinstance(value[1], int)):
            if value[0] >= 0 and value[1] >= 0:
                self.__position = value
            else:
                raise TypeError("position must be a tuple"
                                " of 2 positive integer")
        else:
            raise TypeError("position must be a tuple of 2 positive integer")

    def area(self):
        """Method to to retrieve the area"""
        return self.__size ** 2

    def my_print(self):
        """Method to print the square with #"""
        count = 0
        if self.__size == 0:
            print("")
        else:
            sec = 0
            while sec < self.__position[1]:
                print("")
                sec += 1
            while count < self.__size:
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
                count += 1

    def __str__(self):
        """Method to print the square with # from print()"""
        count = 0
        sq_str = ""
        if self.__size == 0:
            sq_str += '\n'
        else:
            sec = 0
            while sec < self.__position[1]:
                sq_str += '\n'
                sec += 1
            while count < self.__size:
                sq_str += " " * self.__position[0]
                sq_str += "#" * self.__size + '\n'
                count += 1
        return sq_str
