#!/usr/bin/python3
"""
This is a 101-add_attribute module
"""


def add_attribute(cls, name, value):
    """
    Adds a new attribute if possible
    """
    if hasattr(cls, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(cls, name, value)
