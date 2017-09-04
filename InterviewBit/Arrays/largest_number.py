"""

Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""

class Solution:
    def compare(self, a, b):
        ab = str(a) + str(b)
        ba = str(b) + str(a)
        if int(ab) < int(ba):
            return 1
        else:
            return -1
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        arr = sorted(A, cmp=self.compare)

        return int(''.join(str(x) for x in arr))
