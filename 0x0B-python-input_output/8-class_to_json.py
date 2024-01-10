#!/usr/bin/python3
"""Module to convert class to json"""


def class_to_json(obj):
    """Function to serialize python objects
    in json format"""

    dic = {}
    if hasattr(obj, "__dict__"):
        dic = obj.__dict__.copy()
    return dic
