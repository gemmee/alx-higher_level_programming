#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = my_list[:]  # same as my_list.copy()
    if 0 <= idx < len(my_list):
        copy_list[idx] = element
    return copy_list
