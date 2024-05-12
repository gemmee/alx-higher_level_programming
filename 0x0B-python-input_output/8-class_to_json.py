#!/usr/bin/python3
"""
    This is a 8-class_to_json module
"""


def class_to_json(obj):
    """
        Returns the dictionary description with simple data structure for
        JSON serialization of an object
    """
    d = {}
    if hasattr(obj, "__dict__"):
        d = obj.__dict__.copy()
    return d
