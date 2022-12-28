#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    a_dictionary: the dictionary with integers values
    """
    new_dict = {}
    for k in a_dictionary:
        new_dict[k] = a_dictionary[k] * 2
    return new_dict
