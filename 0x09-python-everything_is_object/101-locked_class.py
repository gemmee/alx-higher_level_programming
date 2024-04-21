#!/usr/bin/python3
"""
This module is `101-locked_class`

It has one class `LockedClass`.
"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance variables,
    except if the new instance attribute is called `first_name`
    """
    __slots__ = ('first_name', )
