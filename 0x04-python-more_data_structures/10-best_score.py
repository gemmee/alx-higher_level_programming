#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns a key with a biggest integer value or
    returns None if no integer found

    a_dictionary: the dictionary with integers values
    """
    if a_dictionary is None or a_dictionary == {}:
        return None
    key_max = list(a_dictionary.keys())[0]
    max = a_dictionary[key_max]
    for k in a_dictionary:
        if a_dictionary[k] > max:
            max = a_dictionary[k]
            key_max = k
    return key_max
