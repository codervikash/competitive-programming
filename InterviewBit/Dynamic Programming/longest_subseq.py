"""
Given an array of integers, find the length of longest subsequence which is first increasing then decreasing.

**Example: **

For the given array [1 11 2 10 4 5 2 1]

Longest subsequence is [1 2 10 4 2 1]

Return value 6
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        n = len(A)
        if n == 0:
            return 0
        lis = [1 for row in xrange(n)]
        for i in xrange(1, n):
            for j in xrange(i):
                if A[i] > A[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1

        lds = [1 for row in xrange(n)]
        for i in xrange(n-2, -1, -1): #loop from n-2 downto 0
            for j in xrange( n - 1, i, -1):
                if A[i] > A[j] and lds[i] < lds[j] + 1:
                    lds[i] = lds[j] + 1

        m = 0
        for i in xrange(n):
            m = max(m, (lis[i] + lds[i] - 1))

        return m
