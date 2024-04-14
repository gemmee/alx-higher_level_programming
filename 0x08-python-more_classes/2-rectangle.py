#!/usr/bin/python3
'''
This is '2-rectangle' module.

This module contains 1 class Rectangle
'''


class Rectangle:
    '''
    Defines a Rectangle class

    **Instance attributes**
    width: private, must be a non-negative int
    height: private, must be a non-negative int

    **Public instance methods**
    area(self)
    perimeter(self)
    '''

    def __init__(self, width=0, height=0):
        '''
        Instantiates a Rectangle

        Args:
            width: optional, a non-negative int
            height: optional, a non-negative int
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return 2 * (self.__width + self.__height)
