"""
Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        sum = []
        n = len(A)
        arr = []
        rec = 1
        for i in xrange(n):
            num = A[n - 1 - i] + rec
            if num >= 10:
                rec = 1
                num = num - 10
            else:
                rec = 0

            sum.append(num)

        if rec > 0:
            sum.append(rec)
        found = 0
        dum1 = []
        l = len(sum)
        for i in xrange(l):
            dum1.append(sum[l - 1 - i])
        while dum1[0] == 0:
            dum1.pop(0)
        return dum1
