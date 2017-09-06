"""
Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and column to 0.

Do it in place.

Example

Given array A as

1 0 1
1 1 1
1 1 1
On returning, the array A should be :

0 0 0
1 0 1
1 0 1
Note that this will be evaluated on the extra memory used. Try to minimize the space and time complexity.
"""

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        row = len(A)
        col = len(A[0])
        rowFlag = False
        colFlag = False

        for i in xrange(row):
            if A[i][0] == 0:
                colFlag = True

        for j in xrange(col):
            if A[0][j]== 0:
                rowFlag = True

        for i in xrange(row):
            for j in xrange(col):
                if A[i][j] == 0:
                    A[0][j] = 0
                    A[i][0] = 0

        for i in xrange(1, row):
            for j in xrange(1, col):
                if A[0][j] == 0 or A[i][0] == 0:
                    A[i][j] = 0

        if rowFlag:
            for i in xrange(col):
                A[0][i] = 0

        if colFlag:
            for j in xrange(row):
                A[j][0] = 0

        return A
