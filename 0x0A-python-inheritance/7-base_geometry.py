#!/usr/bin/python3
"""
This is a 7-base_geometry module

It has one class BaseGeometry
"""


class BaseGeometry:
    """
    A class with two public instance methods
    """
    def area(self):
        """Just raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Just raises an exceptions for now"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
