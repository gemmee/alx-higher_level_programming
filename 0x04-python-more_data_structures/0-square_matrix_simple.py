#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    '''
    compute the square value of alll integers of a matrix
    '''
    sqr = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(matrix[i][j] ** 2)
        sqr.append(row)
    return sqr
