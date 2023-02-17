#!/usr/bin/python3
"""
This is 6-load_from_json_file module.

It contains a function that creates an Object from a "JSON file".
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file.

    Args:
        filename - the text file name.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
