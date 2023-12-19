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
        if isinstance(next_node, Node) or next_node == None:
            self.__next_node = next_node
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
    def next_node(self):
        """method to retrieve the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """"method to set new next node"""
        if isinstance(value, Node) or value == None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """class to define a singly linked list"""

    def __init__(self):
        """no variable to instantiate"""
        self.head = None

    def sorted_insert(self, value):
        """insert a new node into correct position"""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next_node != None and
                   current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """print the entire lit to stdout"""
        res = []
        current = self.head
        while current:
            res.append(str(current.data))
            current = current.next_node
        return '\n'.join(res)
