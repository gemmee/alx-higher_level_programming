#!/usr/bin/python3
"""
This is the 2-matrix_divided module

It is composed of a function that divides each elements of a matrix by a number.

A doctest has been created for this module in the /tests directory
It can be run with
python3 -m doctest -v ./tests/2-matrix_divided.txt

"""


def matrix_divided(matrix, div):
    """Divides a matrix by a number.

    Args:
        matrix: must be a list of lists of floats or ints of the same size
        div: the divisor, must be a non 0 number

    Returns:
        a matrix where all values have been divided, rounded to 2 decimal places

    Raises:
        TypeError: if the elements of the matrix aren't lists or,
                   if the elements of the lists aren't integers/floats or,
                   if div is not an integer/float number or,
                   if the lists of the matrix don't have the same size

        ZeroDivisionError: if div is zero

    """
    
    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    length = 0
    msg_size = "Each row of the matrix must have the same size"

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(msg_type)

        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(msg_type)

        if length != 0 and len(elems) != length:
            raise TypeError(msg_size)

        length = len(elems)

    new = [[round(num / div, 2) for num in elems] for elems in matrix]
    return (new)
