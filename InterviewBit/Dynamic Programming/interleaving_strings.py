#!/usr/bin/python

"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example,
Given:

s1 = "aabcc",
s2 = "dbbca",
When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""

class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, A, B, C):
        count1 = {}
        count2 = {}
        count3 = {}
        for each in A:
            if count1.has_key(each):
                count1[each] += 1
            else:
                count1[each] = 1
        for each in B:
            if count2.has_key(each):
                count2[each] += 1
            else:
                count2[each] = 1
        for each in C:
            if count3.has_key(each):
                count3[each] += 1
            else:
                count3[each] = 1

        for each in count3:
            sum1 = 0
            if count1.has_key(each):
                sum1 += count1[each]
            if count2.has_key(each):
                sum1 += count2[each]
            if sum1 != count3[each]:
                return 0

        return 1