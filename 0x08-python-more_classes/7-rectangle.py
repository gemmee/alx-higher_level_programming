#!/usr/bin/python3
'''
This is '7-rectangle' module.

This module contains 1 class Rectangle
'''


class Rectangle:
    '''
    Defines a Rectangle class

    **Private instance attributes**
    width: must be a non-negative int
    height: must be a non-negative int

    **Public class attributes**
    number_of_instances: initialized to 0, non-negative int
    print_symbol: initialized to #, can be any type

    **Public instance methods**
    area(self)
    perimeter(self)
    '''
    number_of_instances = 0
    print_symbol = '#'  # Used as symbol for string representation

    def __init__(self, width=0, height=0):
        '''
        Instantiates a Rectangle

        Args:
            width: optional, a non-negative int
            height: optional, a non-negative int
        '''
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        if (self.__width == 0) or (self.__height == 0):
            return ""
        return '\n'.join(["{}".format(self.print_symbol) *
                         self.__width for h in range(self.__height)])

    def __repr__(self):
        '''Repr of Rectangle'''
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        '''Deletes instance'''
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
