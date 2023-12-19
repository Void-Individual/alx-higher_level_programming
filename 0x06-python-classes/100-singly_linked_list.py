#!/usr/bin/python3
"""This is a class module"""

class Node:
    """Class to define a node in a list"""
    def __init__(self, data, next_node=None):
        """Instantiation of fields"""
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError("data must be an integer")
        if isinstance(next_node, Node):
            self.next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """method to retrieve data"""
        return self.__data

    @data.setter
    def data(self, value):
        """method to reset value of data"""
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property