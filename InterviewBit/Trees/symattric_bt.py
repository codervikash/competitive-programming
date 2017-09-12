"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Example :

    1
   / \
  2   2
 / \ / \
3  4 4  3
The above binary tree is symmetric.
But the following is not:

    1
   / \
  2   2
   \   \
   3    3
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def is_sym_util(self, a, b):
        if a is None and b is None:
            return True

        if a is None or b is None:
            return False

        if self.is_sym_util(a.left, b.right) and self.is_sym_util(a.right, b.left) and a.val == b.val:
            return True

        return False

    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        if A is None:
            return True

        return self.is_sym_util(A.left, A.right)
