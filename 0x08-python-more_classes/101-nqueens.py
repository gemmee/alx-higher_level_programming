#!/usr/bin/python3
'''
This module is 101-nqueens.

It has a solution for the N queens puzzle.
'''
import sys


def solve_nqueens(n, row):
    global solutions
    global col_list
    if row == n:
        solutions.append(col_list[:])  # my goal
    else:
        for col in range(n):
            col_list.append([row, col])  # my choice
            if is_valid():
                solve_nqueens(n, row + 1)
            col_list.pop()  # undo my choice


def is_valid():
    row_id = len(col_list) - 1
    for i in range(row_id):
        diff = abs(col_list[i][1] - col_list[row_id][1])
        if diff == 0 or diff == (row_id - i):
            return False
    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = []
    col_list = []
    n = int(sys.argv[1])
    solve_nqueens(n, 0)
    for sol in solutions:
        print(sol)
