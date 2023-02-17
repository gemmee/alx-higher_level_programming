#!/usr/bin/python3
"""
This a 4-from_json_string module.

It contains one function that returns an object represented by a JSON string.
"""
import json



def from_json_string(my_str):
    """Deserialize a JSON string.

    Args:
        my_str - the JSON string to be deserialized
    Returns:
        an object represented by the JSON
    """
    return json.loads(my_str)
