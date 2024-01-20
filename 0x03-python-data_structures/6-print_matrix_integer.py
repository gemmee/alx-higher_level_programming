#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    for i in range(row):
        col = len(matrix[i])
        for j in range(col):
            sep = '{}'.format('\n' if j == col-1 else ' ')
            print('{:d}'.format(matrix[i][j]), end=sep)
    if row == 1:
        print()
