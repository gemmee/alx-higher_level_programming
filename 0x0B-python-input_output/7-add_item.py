#!/usr/bin/python3
"""
This is module 9-add_item.

This module contains one function that adds all arguments to a python list.
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def load_and_save(filename, args):
    """Loads a json representation of a list, add to it and save it to file.

    Args:
        filename - path to the file
        args - list of arguments to add to a list
    """
    try:
        my_obj = load_from_json_file(filename)
    except FileNotFoundError:
        my_obj = []
    save_to_json_file(my_obj + args, filename)


if __name__ == "__main__":
    filename = "add_item.json"
    load_and_save(filename, sys.argv[1:])
