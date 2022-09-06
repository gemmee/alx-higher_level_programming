#!/usr/bin/python3
def no_c(my_string):

    '''
    A function that removes all characters c and C from a string.
    '''

    newlist = list(my_string)
    count = 0
    for x in newlist:
        if x == 'c' or x == 'C':
            newlist[count] = ""
        count += 1
    return "".join(newlist)
