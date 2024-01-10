#!/usr/bin/python3
"""Module to create a class"""


class Student:
    """custom class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method to retrieve dict format of a student
        instance"""

        dic = {}
        if hasattr(self, "__dict__"):
            dic = self.__dict__.copy()
        return dic
