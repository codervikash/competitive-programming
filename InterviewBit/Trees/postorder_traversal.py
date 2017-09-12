"""
Given a binary tree, return the postorder traversal of its nodes’ values.

Example :

Given binary tree

   1
    \
     2
    /
   3
return [3,2,1].

Using recursion is not allowed.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def peek(self, stack):
        if len(stack) > 0:
            return stack[-1]
        return None
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, root):
        ans = []
        if root is None:
            return

        stack = []

        while(True):

            while (root):
                if root.right is not None:
                    stack.append(root.right)
                stack.append(root)
                root = root.left

            root = stack.pop()

            if (root.right is not None and
                self.peek(stack) == root.right):
                stack.pop()
                stack.append(root)
                root = root.right

            else:
                ans.append(root.val)
                root = None

            if (len(stack) <= 0):
                break
        return ans
