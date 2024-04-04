#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list[:x]:
            print(i, end='')
            count += 1
        print()
        return (count)
    except (IndexError, TypeError):
        print("An error occurred!")
