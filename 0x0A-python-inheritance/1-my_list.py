#!/usr/bin/python3
"""
This is module 1-my_list.
It contains one class that inherits from another class.
A test suite has been developed for this class in the /tests folder
run it with python3 -m doctest ./tests/1-my_list.txt
"""


class MyList(list):
    """Inherits from the list class

    Assumes all the elements in the list are int
    Methods:
        print_sorted - prints the list in ascending order

    """

    def print_sorted(self):
        """prints the list in sorted order"""
        print(sorted(self))
