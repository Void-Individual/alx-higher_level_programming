#!/usr/bin/python3
"""Module to convert json str to an object"""
import json


def from_json_string(my_str):
    """Function to return an object"""

    return json.loads(my_str)
