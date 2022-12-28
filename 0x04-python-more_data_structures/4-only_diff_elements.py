#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.

    set_1: the first set
    set_2: the second set
    """
    return set_1.symmetric_difference(set_2)
