#!/usr/bin/python3
"""
This is module inherits_from
This module contains only one function
"""


def inherits_from(obj, a_class):
    """Evaluates whether an object is an instance of a subclass of a class

    Args:
        obj: an object
        a_class: a class
    Return:
        True if obj is from a sub class of a_class excluding a_class,
        False otherwise
    """
    return (issubclass(type(obj), a_class) and (type(obj) is not a_class))
