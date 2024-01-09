#!/usr/bin/python3
"""Module for my own int class"""


class MyInt(int):
    """An int subclass that inverts == and !="""

    def __init__(self, num):
        """Instantiating the class"""

        if not isinstance(num, int):
            raise Exception
        self.num = num

    def __eq__(self, __value: object) -> bool:
        return super().__ne__(__value)

    def __ne__(self, __value: object) -> bool:
        return super().__eq__(__value)
