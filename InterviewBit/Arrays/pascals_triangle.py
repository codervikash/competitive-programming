"""
Given numRows, generate the first numRows of Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Given numRows = 5,

Return

[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
"""

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        arr = []
        if A == 0:
            return []
        arr.append([1])
        for i in xrange(1, A):
            arr1 = [1]
            for j in xrange(1, i + 1):
                a = arr[i - 1][j - 1]
                if j < len(arr[i - 1]):
                    a += arr[i - 1][j]
                arr1.append(a)
            arr.append(arr1)

        return arr
