#!/usr/bin/python3
"""
    This is a 1-write_file module
"""


def write_file(filename="", text=""):
    """
        Writes a string to a text file (UTF8) and returns
        the number of characters written.
    """
    with open(filename, mode="w", encoding="UTF8") as f:
        chars = 0
        for c in text:
            f.write(c)
            chars += 1
        return chars
