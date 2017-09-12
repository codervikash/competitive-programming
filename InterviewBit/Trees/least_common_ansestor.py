"""

Find the lowest common ancestor in an unordered binary tree given two values in the tree.

 Lowest common ancestor : the lowest common ancestor (LCA) of two nodes v and w in a tree or directed acyclic graph (DAG) is the lowest (i.e. deepest) node that has both v and w as descendants.
Example :


        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2_     0        8
         /   \
         7    4
For the above tree, the LCA of nodes 5 and 1 is 3.

 LCA = Lowest common ancestor
Please note that LCA for nodes 5 and 4 is 5.

You are given 2 values. Find the lowest common ancestor of the two nodes represented by val1 and val2
No guarantee that val1 and val2 exist in the tree. If one value doesn’t exist in the tree then return -1.
There are no duplicate values.
You can use extra memory, helper functions, and can modify the node struct but, you can’t add a parent pointer.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lca_util(self, root, val1, val2, v):
        if root is None:
            return

        if root.val == val1:
            v[0] = True
            return val1

        if root.val == val2:
            v[1] = True
            return val2

        left_lca = self.lca_util(root.left, val1, val2, v)
        right_lca = self.lca_util(root.right, val1, val2, v)

        if left_lca and right_lca:
            return root.val
        # print left_lca, right_lca
        return left_lca if left_lca is not None else right_lca

    def find(self, root, val):
        if root is None:
            return
        if root.val == val:
            return True

        return self.find(root.left, val) or self.find(root.right, val)

    # @param A : root node of tree
    # @param val1 : integer
    # @param val2 : integer
    # @return an integer
    def lca(self, A, val1, val2):
        if A is None:
            return -1

        v = [False, False]
        lca = self.lca_util(A, val1, val2, v)
        # print lca
        # print self.find(A, val1)
        # print self.find(A, val2)
        if v[0] and v[1] or v[0] and self.find(A, val2) or v[1] and self.find(A, val1):
            return lca

        return -1
