# You are given N sticks, where the length of each stick is a positive integer. A cut operation is performed on the sticks such that all of them are reduced by the length of the smallest stick.

# Suppose we have six sticks of the following lengths:

# 5 4 4 2 2 8
# Then, in one cut operation we make a cut of length 2 from each of the six sticks. For the next cut operation four sticks are left (of non-zero length), whose lengths are the following:

# 3 2 2 6
# The above step is repeated until no sticks are left.

# Given the length of N sticks, print the number of sticks that are cut in subsequent cut operations.


# Enter your code here. Read input from STDIN. Print output to STDOUT
def stick(x, y):
    z = len(y)
    b = []
    for a in range(z):
        if y[a] >= x:
            q = y[a] - x
            b.append(q)
        else:
            pass

    c = len(b)
    if c > 1:
        print (c)
        d = filter(lambda t: t != 0, b)
        f = sorted(d)
        e = d[0]
        stick(e, f)

    else:
        print (c)


x = int(raw_input())
y = map(int, raw_input().split())
m = sorted(y)
w = m[0]
stick(w, m)
