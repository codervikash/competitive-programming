"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

 NOTE : The path has to end on a leaf node.
Example :

         1
        /
       2
min depth = 2.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):
        if A is None:
            return 0

        if A.left is None and A.right is None:
            return 1

        if A.left is None:
            return self.minDepth(A.right) + 1
        if A.right is None:
            return self.minDepth(A.left) + 1

        ldepth = self.minDepth(A.left)
        rdepth = self.minDepth(A.right)

        return min(ldepth, rdepth) + 1
