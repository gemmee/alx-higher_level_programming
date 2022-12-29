#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list on the same line followed by a new line.

    my_list: a list that can contain any type
    x: number of elements to print(it can be greater than length of my_list)

    Return: number of elements printed

    Description:
        - You have to use try and except.
        - You are not allowed to import any module.
        - You are allowed to use len()
    """
    try:
        count = 0
        for i in my_list[:x]:
            print(i, end='')
            count += 1
        print()
        return (count)
    except (IndexError, TypeError):
        print("An  error occurred!")
