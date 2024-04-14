#!/usr/bin/python3
'''
Alternative solution for n queens puzzle
'''
from sys import argv, exit

class Solution:
    def solveNQueens(self, n):
        col = set()
        posDiag = set()  # (r + c) is constant
        negDiag = set()  # (r - c) is constant

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)  # recursion

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return res


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
    except Exception:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    nqueens = Solution()
    for solution in nqueens.solveNQueens(n):
        for i in solution:
            print(i)
        print()
