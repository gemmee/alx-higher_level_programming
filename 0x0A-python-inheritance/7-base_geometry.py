#!/usr/bin/python3
"""
This is module 7-base_geometry

This module creates one class
A test suite has been created for this module. Run it with
python3 -m doctest ./tests/7-base_geometry.txt
"""


class BaseGeometry:
    """Class Base Geometry

    Fields:
        None
    Methods:
        area() - raises an Exception
        integer_validator() - validates value.
    """
    def area(self):
        """Raises an exception as it is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the choice of value for name.

        Args:
            name: a name (string)
            value: should be a positive integer
        """
        if type(name) is not str:
            return
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
