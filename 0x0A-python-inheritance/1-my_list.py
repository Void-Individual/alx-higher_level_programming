#!/usr/bin/python3
"""Module for a class that inherits from list"""


class MyList(list):
    """A child class with the aprent class list"""

    def print_sorted(self):
        """Method to print the list in ascention"""
        copied = self.copy()
        sorted_list = sorted(copied)
        print(sorted_list)
