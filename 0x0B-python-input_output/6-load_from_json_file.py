#!/usr/bin/python3
"""Module co create object from json"""
import json


def load_from_json_file(filename):
    """Function that reads a json file and
     creates an object from it"""

    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
