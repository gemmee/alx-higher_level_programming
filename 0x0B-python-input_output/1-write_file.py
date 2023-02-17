#!/usr/bin/python3
"""
This is module 1-write_file.py
It contains only one function.
"""

def write_file(filename="", text=""):
    """Writes a string to a text file and return number of characters written.

    Args:
    	filename - the file, it will be created if it doesn't exist and content is 
                   overidden if it exists
    	text - the string to be written to the file
    """
    with open(filename, "w+", encoding="utf8") as f:
        return f.write(text)
