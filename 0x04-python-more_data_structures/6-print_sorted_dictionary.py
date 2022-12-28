#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.

    a_dictionary: the dictionary
    """
    for k in sorted(a_dictionary.keys()):
        print(f"{k}: {a_dictionary[k]}")
