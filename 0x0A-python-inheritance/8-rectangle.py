#!/usr/bin/python3
"""
This module is 8-rectangle

It has one class Rectangle that inherits from
BaseGeometry class in 7-base_geometry module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Args:
            width: private, must be positive int
            height: private, must be positive int
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
