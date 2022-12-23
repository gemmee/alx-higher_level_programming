#!/bin/usr/python3

def max_integer(my_list=[]):
    """
    Finds and returns the biggest integer of a list.

    my_list: the list
    """
    if len(my_list) == 0:
        return None
    max = my_list[0]
    for item in range(len(my_list)):
        if my_list[item] > max:
            max = my_list[item]
    return max
