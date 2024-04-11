#!/usr/bin/python3
'''
This is a ``3-say_my_name`` module.
It supplies one function, say_my_name.
'''


def say_my_name(first_name, last_name=""):
    '''Prints `My name is <first name> <last name>`

    Args:
        first_name: the first name, must be a string
        last_name: the last name, must be a string
    Returns:
        None
    Raises:
        TypeError: if first_name or last_name is not a string
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f'My name is {first_name} {last_name}')
