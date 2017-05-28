#!/bin/python

import sys

def solve(a):
    n = len(a)
    sum1 = sum2 = 0
    for i in xrange(n/2):
        sum1 = sum1 + a[i]
        sum2 = sum2 + a[n - i - 1]
    return abs(sum1 - sum2)

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
result = solve(a)
print(result)