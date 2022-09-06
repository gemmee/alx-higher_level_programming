#!/usr/bin/python3
def no_c(my_string):

    '''
    A function that removes all characters c and C from a string.
    '''

    newlist = list(my_string)
    for x in newlist:
        if x == 'c':
            newlist.remove('c')
        if x == 'C':
            newlist.remove('C')
    my_string = "".join(newlist)
    return my_string
