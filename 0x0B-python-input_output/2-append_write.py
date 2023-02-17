#!/usr/bin/python3
"""
This module is 2-append_write.

It has one function that appends a string at the end of a text file
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file.

    Args:
        filename - the text file to be modified
                    It will be created if it doesn't exist.
        text - the string to be appended to the file.
    Returns:
        the number of characters added.
    """
    with open(filename, "a+", encoding="utf-8") as f:
        return f.write(text)
