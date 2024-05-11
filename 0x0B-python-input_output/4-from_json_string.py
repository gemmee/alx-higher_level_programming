#!/usr/bin/python3
"""
    This is a 4-from_json_string module
"""
import json


def from_json_string(my_str):
    """
        Returns an object represented by a JSON string
    """
    return json.loads(my_str)
