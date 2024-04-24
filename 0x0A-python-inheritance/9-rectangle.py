#!/usr/bin/python3
"""
This is a  9-rectangle module

It has Rectangle class that inherits from BaseGeometry class that
is in another module 7-base_geometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of Rectangle"""
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height)
