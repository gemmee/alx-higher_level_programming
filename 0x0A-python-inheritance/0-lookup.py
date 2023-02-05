#!/usr/bin/python3
"""
This is module 0-lookup.
It only contains one function.
"""


def lookup(obj):
    """Lists all the available attributes and methods of an object.

    Args:
        obj: any object
    Returns:
        a list
    """
    return dir(obj)
