#!/usr/bin/python3
"""
    12-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of rows of pascal triangle
    """
    row = [1]
    temp = [0]
    pascal = []

    if n <= 0:
        return pascal

    for i in range(n):
        pascal.append(row)
        row = [n + m for n, m in zip(row + temp, temp + row)]
    return pascal

n = 5
for row in pascal_triangle(5):
    print(row)
