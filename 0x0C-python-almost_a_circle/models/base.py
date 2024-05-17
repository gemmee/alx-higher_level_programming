#!/usr/bin/python3
"""
    This is a base module
"""


class Base:
    """
    Represent the base model.

    Represents the "base" for all other classes in project 0x0C*.

    Attributes:
        _nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
