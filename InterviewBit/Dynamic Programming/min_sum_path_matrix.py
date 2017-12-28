"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

 Note: You can only move either down or right at any point in time.
Example :

Input :

    [  1 3 2
       4 3 1
       5 6 1
    ]

Output : 8
     1 -> 3 -> 2 -> 1 -> 1
"""

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        n = len(A) - 1
        m = len(A[0]) - 1

        d = [[0 for col in xrange(m + 1)] for row in xrange(n + 1)]
        d[0][0] = A[0][0]

        for i in xrange(1, n + 1):
            d[i][0] = A[i][0] + d[i - 1][0]

        for j in xrange(1, m + 1):
            d[0][j] = A[0][j] + d[0][j - 1]

        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                d[i][j] = min(d[i][j - 1], d[i - 1][j]) + A[i][j]


        return d[n][m]
