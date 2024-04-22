#!/usr/bin/python3
"""
This is module 4-inherits_from

It contains one function inherits_from
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    return False 
