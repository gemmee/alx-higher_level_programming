#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers.

    my_list: the list
    x: the number of elements to access in my_list.

    Return: the number of elements printed
    Description:
        x can be bigger than the length of my_list - if it's the case, an
        exception is expected to occur.
        All integers have to printed on the same line followed by a new line,
        - other type of value in the list must be skipped(in silence).
        You are not allowed to import any module.
        You are not allowed to use len().
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (count)

