"""
Given A, how many structurally unique BST’s (binary search trees) that store values 1...A?

Example :

Given A = 3, there are a total of 5 unique BST’s.


   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""
class Solution:
    def num_tree(self, n, solution):
        if n < 0:
            return 0
        elif n == 0 or n == 1:
            return 1

        posiblities = 0
        for i in xrange(n):
            if solution[i] == -1:
                solution[i] = self.num_tree(i, solution)
            if solution[n - i - 1] == -1:
                solution[n - i - 1] = self.num_tree(n - i - 1, solution)

            posiblities += solution[i] * solution[n - i - 1]

        return posiblities

    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        solution = [-1] * A
        return self.num_tree(A, solution)
