"""
Write a function to find the longest common prefix string amongst an array of strings.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Given the array of strings, you need to find the longest S which is the prefix of ALL the strings in the array.

Example:

Given the array as:

[

  "abcdefgh",

  "aefghijk",

  "abcefgh"
]
The answer would be “a”.
"""

import sys
class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        l = len(A)
        if l == 1:
            return A[0]
        min_length = sys.maxint
        result = []
        for i in xrange(l):
            min_length = min(len(A[i]), min_length)

        i = 0
        while i < min_length:
            similar = False
            for j in xrange(1, l):
                similar = False
                if A[j - 1][i] == A[j][i]:
                    similar = True
            if similar:
                result.append(A[j - 1][i])
                i += 1
            else:
                break

        return ''.join(result)
