"""
Given an array of integers, every element appears thrice except for one which occurs once.

Find that element which does not appear thrice.

Note: Your algorithm should have a linear runtime complexity.

Could you implement it without using extra memory?

Example :

Input : [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
Output : 4
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        l = len(A)
        result = 0

        for i in xrange(32):
            sum = 0
            x = (1 << i)
            for j in xrange(l):
                if A[j] & x:
                    sum += 1
            if sum % 3:
                result |= x

        return result
