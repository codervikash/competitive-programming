#!/usr/bin/python

"""
Given an array where every element occurs three times, except one element which occurs only once. Find the element that occurs once. Expected time complexity is O(n) and O(1) extra space.
Examples:

Input: arr[] = {12, 1, 12, 3, 12, 1, 1, 2, 3, 3}
Output: 2
"""

def get_single_element(arr):
    l = len(arr)
    for i in xrange(l):
        


arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 2, 2, 3, 7]
print 'element apering only once: '
print get_single_element(arr)