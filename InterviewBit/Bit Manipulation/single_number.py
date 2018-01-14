"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example :

Input : [1 2 2 3 1]
Output : 3
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        xor = A[0]
        for i in xrange(1, len(A)):
            xor ^= A[i]

        return xor
