#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    key: the key which is always a string
    value: the value which can be of any type

    Description:
        If a key exists in the dictionary, the value will be replaced
        If a key doesn’t exist in the dictionary, it will be created
    """
    a_dictionary[key] = value
    return a_dictionary
