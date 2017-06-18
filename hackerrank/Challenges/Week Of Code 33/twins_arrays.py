#!/usr/bin/python

"""
You are given two arrays  and  each containing  integers. You need to choose exactly  number from A and exactly  number from B such that the index of the two chosen numbers is not same and the sum of the 2 chosen values is minimum.

Your objective is to find and print this minimum value.
"""

import sys

def twinArrays(ar1, ar2):
    max1, max2 = (ar1[0], ar1[1]) if ar1[0] < ar1[1] else (ar1[1], ar1[0])
    ind1, ind2 = (0,1) if ar1[0] < ar1[1] else (1,0)
    max3, max4 = (ar2[0], ar2[1]) if ar2[0] < ar2[1] else (ar2[1], ar2[0])
    ind3, ind4 = (0,1) if ar2[0] < ar2[1] else (1,0)
    for i in xrange(2, len(ar1)):
        if ar1[i] < max1:
            max1, max2 = ar1[i], max1
            ind1, ind2 = i, ind1
        elif ar1[i] < max2:
            max2 = ar1[i]
            ind2 = i
        if ar2[i] < max3:
            max3, max4 = ar2[i], max3
            ind3, ind4 = i, ind3
        elif ar2[i] < max4:
            max4 = ar2[i]
            ind4 = i
    
    if ind1 != ind3:
        return (max1 + max3)
    else:
        return min(max1 + max4, max2 + max3)

n = int(raw_input().strip())
ar1 = map(int, raw_input().strip().split(' '))
ar2 = map(int, raw_input().strip().split(' '))
result = twinArrays(ar1, ar2)
print(result)
