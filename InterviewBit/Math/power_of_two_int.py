"""
Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

Example

Input : 4
Output : True
as 2^2 = 4.
"""

import math

class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        if A <= 1:
            return True
        for a in xrange(2, int(math.sqrt(A)) + 1):
            p = math.log(A)/math.log(a)
            if(p - int(p) < 0.000000001):
                return True

        return False
