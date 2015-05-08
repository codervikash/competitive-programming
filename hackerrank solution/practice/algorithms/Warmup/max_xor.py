# Given two integers, L and R, find the maximal value of A xor B, where A and B satisfy the following condition:

# L≤A≤B≤R


#!/bin/python

# Complete the function below.


def  maxXor( l,  r):
    a = 0
    for i in range(l ,r+1):
        for j in range(l,r+1):
            b = i ^ j
            if b > a: a = b

    return a


_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)