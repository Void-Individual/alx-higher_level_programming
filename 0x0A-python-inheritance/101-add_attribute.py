#!/usr/bin/python3
"""Module for a function to add attributes"""


def add_attribute(cl, att, value):
    """Function to add a new attribute to a class if it is
     allowed to and if the parameters are allowed"""

    if not isinstance(att, str):
        raise TypeError("can't add new attribute")

    try:
        cl.__dict__[att] = value
    except Exception:
        raise TypeError("can't add new attribute")
