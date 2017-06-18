#!/usr/bin/python

"""
Given an array of distinct integers, find if there are two pairs (a, b) and (c, d) such that a+b = c+d, and a, b, c and d are distinct elements. If there are multiple answers, then print any of them.
"""

def find_element(arr):
    l = len(arr)
    sum_hash = {}

    for i in xrange(l):
        for j in xrange(i + 1, l):
            s = arr[i] + arr[j]
            if sum_hash.has_key(s):
                return sum_hash[s], (i, j)
            else:
                sum_hash[s] = (i, j)


arr = [3, 5, 7, 1, 2, 9, 8]
print find_element(arr)