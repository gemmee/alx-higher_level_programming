#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
matrix2 = [[1]]
print_matrix_integer(matrix2)

print("--")
matrix3 = [[1], [2], [3], [4]]
print_matrix_integer(matrix3)

print("--")
print_matrix_integer()
print("--")
print_matrix_integer([[]])
