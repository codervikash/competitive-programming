"""

Given a binary tree, return the inorder traversal of its nodes’ values.

Example :
Given binary tree

   1
    \
     2
    /
   3
return [1,3,2].

Using recursion is not allowed.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        current = A
        stack = []
        done = 0
        list = []
        while(not done):
            if current:
                stack.append(current)
                current = current.left
            else:
                if len(stack) > 0:
                    current = stack.pop()
                    list.append(current.val)
                    current = current.right
                else:
                    done = 1

        return list
