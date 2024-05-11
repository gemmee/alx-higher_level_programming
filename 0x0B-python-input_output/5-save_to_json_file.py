#!/usr/bin/python3
"""
    This is a 5-save_to_json_file module
"""
import json


def save_to_json_file(my_obj, filename):
    """
        Writes an Object to a text file, using JSON representation
    """
    with open(filename, mode="a", encoding="UTF8") as f:
        f.write(json.dumps(my_obj))
