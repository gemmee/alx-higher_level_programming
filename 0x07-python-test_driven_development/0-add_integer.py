#!/usr/bin/python3
'''
This is the "0-add_integer" module

The 0-add_integer module supplies one function, add_integer().
For example,
>>> add_integer(3, -1)
2
'''


def add_integer(a, b=98):
    '''A function that adds two numbers'''
    if type(a) is int or type(a) is float:
        a = int(a) if type(a) is float else a
    else:
        raise TypeError("a must be an integer")
    if type(b) is int or type(b) is float:
        b = int(b) if type(b) is float else b
    else:
        raise TypeError("b must be an integer")
    return a + b
