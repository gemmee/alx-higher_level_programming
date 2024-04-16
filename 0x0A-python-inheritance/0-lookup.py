#!/usr/bin/python3
'''
This is a 0-lookup module
It has one function lookup
'''


def lookup(obj):
    '''Returns a list available attributes and methods of an object'''
    return dir(obj)
