#!/usr/bin/python3
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

        if isinstance(position[0], int) and isinstance(position[1], int):
            if position[1] >= 0 and position[1] >= 0:
                self.__position = position
            else:
                TypeError("position must be a tuple of 2 positive integers")
        else:
            TypeError("position must be a tuple of 2 positive integers")

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
        if (isinstance(value, tuple) and isinstance(value[0], int)
            and isinstance(value[1], int)):
            if value[0] >= 0 and value[1] >= 0:
                self.__position = value
            else:
                TypeError("position must be a tuple of 2 positive integers")
        else:
            TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Method to to retrieve the area"""
        return self.__size ** 2

    def my_print(self):
        """Method to print the square with #"""
        count = 0
        while count < self.__size:
            val = 0
            pos = 0
            while pos < self.__position[0]:
                print(" ", end='')
                pos += 1
            while val < self.__size:
                print("#", end='')
                val += 1
            print('\n', end='')
            count += 1
