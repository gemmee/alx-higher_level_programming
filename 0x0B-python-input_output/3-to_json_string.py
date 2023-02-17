#!/usr/bin/python3
"""
This is 3-to_json_string module

It contains one function that returns a JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """Returns a JSON representation of an object.

    Args:
        my_obj - the object to be serialized
    Returns:
        the JSON format of the object
    """
    return json.dumps(my_obj)
