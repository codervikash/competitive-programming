"""

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example :

Input : 3
Return : 3

Steps : [1 1 1], [1 2], [2 1]
"""

class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        n = A
        if n == 0:
            return 0
        stair = [0 for x in xrange(n + 1)]
        stair[0] = 1
        stair[1] = 2

        for i in xrange(2, n):
            stair[i] = stair[i - 1] + stair[i - 2]

        return stair[n - 1]
