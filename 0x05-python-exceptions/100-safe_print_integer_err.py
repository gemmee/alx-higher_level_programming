#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """
    Prints an integer safely, otherwise handle errors

    value: anything

    Return: True if value is an int, False otherwise.
    """
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (False)
    else:
        return (True)
