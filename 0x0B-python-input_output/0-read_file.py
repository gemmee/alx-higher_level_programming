#!/usr/bin/python3
"""
    This is a 0-read_file module
"""


def read_file(filename=""):
    """
        Reads a text file(UTF8) and prints it to stdout
    """
    with open(filename, encoding="UTF8") as f:
        print(f.read(), end="")
