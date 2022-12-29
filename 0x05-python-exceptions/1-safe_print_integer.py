#!/usr/bin/python3
def safe_print_integer(value):
    '''
    Prints an integer with '{:d}.format()' followed by a new line

    value: the value to printed

    Return: True if value has been correctly printed, otherwise False

    Description:
        You are not allowed to import any module
        You are not allowed to use type()
        Value can be any type (integer, string, etc.)
    '''
    try:
        if value is not int:
            raise TypeError
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
