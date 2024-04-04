#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    Executes a function safely.

    fct: a pointer to a function
    args: list of arguments

    Return: the result of the function or None if error occurs.
    """
    result = None
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return (result)
