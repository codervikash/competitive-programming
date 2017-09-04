"""
You are in an infinite 2D grid where you can move in any of the 8 directions :

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)

You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

"""

class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        min_steps = 0
        if len(X) == 1 or len(Y) == 1:
            return 0
        for i in xrange(1, len(X)):
            min_steps += max(abs(X[i] - X[i - 1]), abs(Y[i] - Y[i - 1]))

        return min_steps
