"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Given n = 3,

You should return the following matrix:

[
  [ 1, 2, 3 ],
  [ 8, 9, 4 ],
  [ 7, 6, 5 ]
]
"""

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        result = [[0 for i in xrange(A)] for j in xrange(A)]
        start_row = start_col = 0
        end_row = end_col = A - 1
        last_value = 0

        while start_row < A and start_col < A:
            for i in xrange(start_col, end_col + 1):
                last_value = last_value + 1
                result[start_row][i] = last_value
            start_row += 1

            for i in xrange(start_row, end_row + 1):
                last_value = last_value + 1
                result[i][end_col] = last_value
            end_col -= 1


            if start_row < end_row:
                for i in xrange(end_col, start_col - 1, - 1):
                    last_value = last_value + 1
                    result[end_row][i] = last_value
                end_row -= 1


            if start_col < end_col:
                for i in xrange(end_row, start_row - 1, -1):
                    last_value = last_value + 1
                    result[i][start_col] = last_value
                start_col += 1

        return result
