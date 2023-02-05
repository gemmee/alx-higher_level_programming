#!/usr/bin/python3
"""
This is module 0-read_file.
This module contains only one function.
"""


def read_file(filename=""):
    """Reads and prints a file.

    Args:
        filename: path to file, may or not be valid
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
