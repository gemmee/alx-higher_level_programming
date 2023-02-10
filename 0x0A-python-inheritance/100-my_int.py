#!/usr/bin/python3
"""
This is module 100-my_int

This module contains a rebel class
"""


class MyInt(int):
    """ MyInt inherits from int
    """
    def __init__(self, number):
        self.number = number

    def __ne__(self, value):
        return (self.number == value)

    def __eq__(self, value):
        return (self.number != value)

    def __str__(self):
        return (str(self.number))
