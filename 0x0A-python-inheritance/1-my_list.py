#!/usr/bin/python3
'''
This is a 1-my_list module

It contains one class MyList
'''


class MyList(list):
    '''A class that inherits from list'''
    def print_sorted(self):
        '''Prints the list in anscending order'''
        print(sorted(self))
