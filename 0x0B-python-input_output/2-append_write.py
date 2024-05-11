#!/usr/bin/python3
"""
    This is a 2-append_write module
"""


def append_write(filename="", text=""):
    """
        Appends a string at the end of a text file (UTF8) and returns
        the number of characters added
    """
    with open(filename, mode="a", encoding="UTF8") as f:
        chars = 0
        for c in text:
            f.write(c)
            chars += 1
        return chars
