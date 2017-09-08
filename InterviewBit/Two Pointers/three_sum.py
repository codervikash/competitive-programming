"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.

Assume that there will only be one solution

Example:
given array S = {-1 2 1 -4},
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
"""

import sys
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        l = len(A)
        A = sorted(A)
        diff = sys.maxint
        result = 0

        for i in xrange(l - 2):
            j = i + 1
            k = l - 1
            while j < k:
                three_sum = A[i] + A[j] + A[k]
                temp_diff = three_sum - B
                if temp_diff == 0:
                    return B
                if abs(temp_diff) < diff:
                    diff = abs(temp_diff)
                    result = three_sum
                if temp_diff < 0:
                    j += 1
                else:
                    k -= 1

        return result
