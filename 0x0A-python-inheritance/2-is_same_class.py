#!/usr/bin/python3
"""
This module is 2-is_same_class

It has one function is_same_class
"""


def is_same_class(obj, a_class):
    """
    returns True if object is an instance of specified class
    Args:
        obj: object being checked
        a_class: class
    """
    if type(obj) is a_class:
        return True
    return False
