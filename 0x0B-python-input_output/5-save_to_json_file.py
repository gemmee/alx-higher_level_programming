#!/usr/bin/python3
"""
This is 5-save_to_json_file module.

It contains only one function that writes an object to a text file,
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj - the object
        filename - the text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))  # or json.dump(my_obj, f)
