#!/usr/bin/python3
"""
This is module 8-rectangle

This module contains one class Rectangle that inherits from another module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry

    Fields:
        width: private
        height: private
    Methods:
        __init__ - initializes the Rectangle.
    """

    def __init__(self, width, height):
        """Instantiates a Rectangle

        Args:
            width: must be positive int
            height: must be positive int
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
