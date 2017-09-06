"""
You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.
"""

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, arr):
        arr = list(arr)
        n = [0] * 2
        size = len(arr)

        for i in xrange(size):
            if arr[abs(arr[i])-1] > 0:
                arr[abs(arr[i])-1] = -arr[abs(arr[i])-1];
            else:
                n[0] = (abs(arr[i]));

        for i in xrange(size):
            if arr[i]>0:
                n[1] = (i+1);

        return n
