#!/usr/bin/python3
"""
This module is 3-is_kind_of_class

It contains one function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class

    Args:
        obj: the object to be checked
        a_class: class
    """
    if isinstance(obj, a_class):
        return True
    return False
