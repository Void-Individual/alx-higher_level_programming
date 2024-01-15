#!/usr/bin/python3
"""Module to represent a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class square that inherits from the class rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation that stretches to the parent class"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Method to retrieve the size"""

        return self.width

    @size.setter
    def size(self, value):
        """Method to change the value of size"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method to update attributes from variable arguments"""

        if args:
            attr = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Method to return dict format of attributes"""

        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
