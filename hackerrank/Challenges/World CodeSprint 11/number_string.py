#!/bin/python

import sys

def getMagicNumber(s, k, b, m):
    n = len(s)
    sum = 0
    for i in xrange(n - k + 1):
        sum = sum + (int(s[i: i + k], b) % m)
        
    return sum

s = raw_input().strip()
k, b, m = raw_input().strip().split(' ')
k, b, m = [int(k), int(b), int(m)]
result = getMagicNumber(s, k, b, m)
print(result)
