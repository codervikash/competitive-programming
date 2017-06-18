#!/usr/bin/python

"""
A string s contains many patterns of the form 1(0+)1  where 0+ represents any non-empty consecutive sequence of 0's. The patterns are allowed to overlap.

For example, consider string 1101001, we can see there are two consecutive sequences 1(0)1 and 1(00)1 which are of the form 1(0+)1.

You have to answer  queries, each containing a string s. For each query, find and print the total number of patterns of the form 1(0+)1 that occur in s.
"""

def patternCount(s):
    count = 0
    found = 0
    one = 0
    for i in xrange(len(s)):
        if s[i] == '1' and found and one:
            count += 1
            one = 0
        elif s[i] == '1':
            found = 1
            one = 0
        elif s[i] not in ['0', '1']:
            found = 0
            one = 0
        elif s[i] == '0' and found:
            one = 1
        else:
            continue

    return count

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = patternCount(s)
    print(result)