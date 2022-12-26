#!/bin/usr/python3

def printReverse():
    '''
    prints the ASCII alphabet, in reverse order, alternating lowercase
    and uppercase.

    '''
    for i in range(90, 64, -1):
        print("{}".format(chr(i) if i % 2 else chr(i + 32)), end='')


printReverse()
