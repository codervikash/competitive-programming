# Problem Statement

# Alex is attending a Halloween party with his girlfriend, Silvia. At the party, Silvia spots the corner of an infinite chocolate bar (two dimensional, infinitely long in width and length).

# If the chocolate can be served as only 1 x 1 sized pieces and Alex can cut the chocolate bar exactly K times, what is the maximum number of chocolate pieces Alex can cut and give Silvia?

# Input Format
# The first line contains an integer T, the number of test cases. T lines follow.
# Each line contains an integer K.

# Output Format
# T lines; each line should contain an integer that denotes the maximum number of pieces that can be obtained for each test case.

# Constraints
# 1≤T≤10
# 2≤K≤107

# Note: Chocolate must be served in 1 x 1 sized pieces. Alex can't relocate any of the pieces, nor can he place any piece on top of another.

# Enter your code here. Read input from STDIN. Print output to STDOUT


def halloween(a):
    result = 0
    if a % 2 == 0:
        result = (a / 2) * (a / 2)
    else:
        result = ((a + 1) / 2) * (a / 2)
    return result


a = int(raw_input())
for i in range(a):
    b = int(raw_input())
    result = halloween(b)
    print (result)
