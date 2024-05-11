#!/usr/bin/python3
"""
    This is a 6-load_from_json_file module
"""
import json


def load_from_json_file(filename):
    """
        Creates an Object from a JSON file
    """
    with open(filename, encoding="UTF8") as f:
        return json.loads(f.read())
