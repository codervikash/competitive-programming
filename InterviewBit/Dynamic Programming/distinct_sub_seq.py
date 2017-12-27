"""
Given two sequences S, T, count number of unique ways in sequence S, to form a subsequence that is identical to the sequence T.

 Subsequence : A subsequence of a string is a new string which is formed from the original string by deleting some (can be none ) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
Example :

S = "rabbbit"
T = "rabbit"
Return 3. And the formations as follows:

S1= "ra_bbit"
S2= "rab_bit"
S3="rabb_it"
"_" marks the removed character.
"""

class Solution:
    # @param S : string
    # @param T : string
    # @return an integer
    def numDistinct(self, S, T):
        n = len(S)
        m = len(T)
        d = [[0 for col in xrange(n + 1)] for row in xrange(m + 1)]

        for i in xrange(m + 1):
            for j in xrange(n + 1):
                if i == 0:
                    d[i][j] = 1
                elif j == 0:
                    d[i][j] = 0
                elif T[i - 1] != S[j - 1]:
                    d[i][j] = d[i][j - 1]
                else:
                    d[i][j] = d[i][j - 1] + d[i - 1][j - 1]

        return d[m][n]
