#!/usr/bin/python3
"""
This is a 100-my_int module

It has one class MyInt which inherits from int.
"""


class MyInt(int):
    """MyInt inherits from int"""
    def __init__(self, num):
        self.number = num

    def __eq__(self, value):
        """Invertes the == operator"""
        return self.number != value

    def __ne__(self, value):
        """Invertes the != operator"""
        return self.number == value

    def __str__(self):
        return str(self.number)
