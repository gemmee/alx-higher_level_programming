#!/usr/bin/python3
def no_c(my_string):
    '''
    Removes all characters c and C from a string.
    Without using str.replace()

    my_string: the string to be modified
    '''
    str = "" 
    for x in my_string:
        if x not in "cC":
            str += x
    return str
        
