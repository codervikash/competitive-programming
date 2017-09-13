"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example :

Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

Rain water trapped: Example 1

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, arr):
        l = len(arr)
        lmax = [0] * l
        rmax = [0] * l
        water = 0

        lmax[0] = arr[0]
        for i in xrange(1, l):
            if arr[i] > lmax[i - 1]:
                lmax[i] = arr[i]
            else:
                lmax[i] = lmax[i - 1]

        rmax[l - 1] = arr[l - 1]
        for i in xrange(l - 2, -1, -1):
            if arr[i] > rmax[i + 1]:
                rmax[i] = arr[i]
            else:
                rmax[i] = rmax[i + 1]

        for i in xrange(l):
            water += min(lmax[i], rmax[i]) - arr[i]


        return water
