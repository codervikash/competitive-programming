"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

N Queens: Example 1

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens’ placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        n=A
        stack, res = [[(0, i)] for i in range(n)], []
        while stack:
            board = stack.pop()
            row = len(board)
            if row == n:
                res.append([''.join('Q' if i == c else '.' for i in range(n))
                            for r, c in board])
            for col in range(n):
                if all(col != c and abs(row-r) != abs(col-c)for r, c in board):
                    stack.append(board+[(row, col)])
        return res
