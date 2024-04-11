#!/usr/bin/python3
'''
This is the ``4-print_square`` module.

It supplies one function, print_square().
'''


def print_square(size):
    '''Prints a square with the character `#`.

    Args:
        size: the size length of the square, must be an int
    Returns:
        None
    Raises:
        TypeError: if size is not an integer
                   or if size is a float and is less 0
        ValueError: if size is less than 0
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size:
        print("\n".join(["".join(["#" for i in range(size)])
              for j in range(size)]))
