#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for i in my_list[:x]:
            print(my_list[i], end='')
            i += 1
        print()
        return (i)
    except (IndexError, TypeError):
        print("An error occurred!")
