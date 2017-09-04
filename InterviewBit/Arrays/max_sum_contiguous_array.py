"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example:

Given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the maximum sum.
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        l = len(A)
        if l < 1:
            return 0
        max_ending_here = A[0]
        max_so_far = A[0]

        for i in xrange(1, l):
            max_ending_here = max(max_ending_here + A[i], A[i])

            max_so_far = max(max_ending_here, max_so_far)

        return max_so_far
