#!/usr/bin/python3
"""
    This is a 12-pascal_triangle module
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal's triangle of n
    """
    pascal = []
    if n <= 0:
        return pascal

    for i in range(1, n + 1):
        # print("While i = ", i)
        if i == 1:
            pascal.append([1])
        else:
            if len(pascal) == 1:
                pascal.append([1, 1])
            else:
                elem = pascal[-1].copy()
                count = 1
                new = elem[:]
                while len(new) < i:
                    new[count] = elem[count] + elem[count - 1]
                    count += 1
                    if count == i - 1:
                        new.append(1)
                pascal.append(new)
        # print(pascal)
    return pascal
