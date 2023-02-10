#!/usr/bin/python3
"""
This is module 9-rectangle

This module contains one class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry.

    Fields:
        width: private
        height: private

    Methods:
        area
        __str__
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

    def area(self):
        """Computes area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a nice string about the rectangle"""
        return "[Rectangle] {w}/{h}".format(w=self.__width, h=self.__height)
