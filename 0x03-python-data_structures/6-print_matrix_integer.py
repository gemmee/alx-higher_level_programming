#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    '''
    A function that prints a matrix of integers without importing any module
    Casting integers into strings is not allowed and you have to use
    str.format() to print the integers.
    '''
    if not matrix:
        print()
    else:
        for row in range(len(matrix)):
            for item in range(len(matrix[row])):
                if item != len(matrix[row]) - 1:
                    endspace = ' '
                else:
                    endspace = '\n'
                print("{:d}".format(matrix[row][item]), end=endspace)
