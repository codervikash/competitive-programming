"""
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2
for the pair (3, 4)
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        l = len(A)
        if l < 1:
            return -1
        lmin = [0] * (l)
        rmax = [0] * (l)
        lmin[0] = A[0]
        for i in xrange(1, l):
            lmin[i] = min(lmin[i - 1], A[i])

        rmax[l - 1] = A[l - 1]
        for i in xrange(l - 2, -1, -1):
            rmax[i] = max(rmax[i + 1], A[i])

        i = 0
        j = 0
        max_diff = - 1
        while i < l and j < l:
            if lmin[i] <= rmax[j]:
                max_diff = max(max_diff, (j - i))
                j += 1
            else:
                i += 1

        return max_diff
