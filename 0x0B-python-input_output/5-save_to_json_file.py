#!/usr/bin/python3
"""Module to save an object as txt file in json"""
import json


def save_to_json_file(my_obj, filename):
    """Function to convert obj to json"""

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
