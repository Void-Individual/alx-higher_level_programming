#!/usr/bin/python3
"""Module to create a class"""


class Student:
    """custom class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method to retrieve dict format of a student
        instance"""

        object = self.__dict__.copy()

        if type(attrs) is list:
            for item in attrs:
                if type(item) is not str:
                    return object
            dic = {}
            for find in range(len(attrs)):
                for check in object:
                    if attrs[find] == check:
                        dic[check] = object[check]
            return dic
        return object

    def reload_from_json(self, json):
        """Method to replace the attributes of the instance"""

        for atr in json:
            self.__dict__[atr] = json[atr]
