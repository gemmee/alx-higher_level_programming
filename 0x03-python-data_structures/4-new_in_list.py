#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position without modifying
    the original list(like in C).

    my_list: reference to the original list
    idx: index of at which element is replaced
    element: new element for replace
    """
    copy_list = my_list.copy()
    if 0 <= idx < len(my_list):
        copy_list[idx] = element
    return copy_list
