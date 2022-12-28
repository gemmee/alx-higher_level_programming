#!/usr/bin/python3
def number_keys(a_dictionary):
    """
    Returns the number of keys in a dictionary.

    a_dictionary: the dictionary
    """
    count = 0
    for k in a_dictionary:
        count += 1
    return count
