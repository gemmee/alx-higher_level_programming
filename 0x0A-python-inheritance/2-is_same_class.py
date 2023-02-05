#!/usr/bin/python3
"""
This is module 2-is_same_class
This module only defines one funtion
"""


def is_same_class(obj, a_class):
    """Evaluates whether an object belongs to this class exactly

    Args:
        obj: an object
        a_class: a class
    Returns:
        True if the object is exactly an instance of the class, False otherwise
    """
    return type(obj) == a_class
