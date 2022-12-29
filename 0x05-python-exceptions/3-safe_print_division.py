#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides 2 integers and prints the result.

    a: an integer
    b: an integer

    Return: the value of division or None if failed

    Descripton:
        You have to use try: / except: / finally:
        You have to use "{}".format() to print the result
        You are not allowed to import any module
        The result should print on the finally: section preceded
        by 'Inside result:'
    """
    try:
        div = a / b
    except (ZeroDivisionError, TypeError):
        div = None
    finally:
        print("Inside result: {}".format(div))
        return div
