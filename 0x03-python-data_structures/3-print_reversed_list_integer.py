#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    prints all integers of a list, in reverse order.

    """
    if type(my_list) is list:
        my_list.reverse()
        for index in my_list:
            print("{:d}".format(index))
