#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    key: the key which is always a string
    a_dictionary: the dictionary

    Description:
        If a key doesn’t exist, the dictionary won’t change
        You are not allowed to import any module
    """
    if key in a_dictionary.keys():
        del a_dictionary[key]
    return a_dictionary
