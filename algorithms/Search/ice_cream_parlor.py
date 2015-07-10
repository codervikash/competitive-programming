# Problem Statement

# Sunny and Johnny together have M dollars they want to spend on ice cream. The parlor offers N flavors, and they want to choose two flavors so that they end up spending the whole amount.

# You are given the cost of these flavors. The cost of the ith flavor is denoted by ci. You have to display the indices of the two flavors whose sum is M.

# Input Format

# The first line of the input contains T; T test cases follow.
# Each test case follows the format detailed below: The first line contains M. The second line contains N. The third line contains N space-separated integers denoting the price of each flavor. Here, the ith integer denotes ci.

# Output Format

# Output two integers, each of which is a valid index of a flavor. The lower index must be printed first. Indices are indexed from 1 to N.c


# Enter your code here. Read input from STDIN. Print output to STDOUT


def icecream(a, b, c):
    for i in range(b - 1):
        for j in range(1, b):
            if c[i] + c[j] == a:
                x = [i + 1, j + 1]
                return " ".join(map(str, x))


x = int(raw_input())

for i in range(x):
    y = int(raw_input())
    z = int(raw_input())
    a = [int(i) for i in raw_input().split()]
    answer = icecream(y, z, a)
    print(answer)
