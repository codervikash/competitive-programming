"""
Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from left to right, then right to left for the next level and alternate between).

Example :
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return

[
         [3],
         [20, 9],
         [15, 7]
]
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        if A is None:
            return []
        q = deque()
        q.append(A)
        zig = False
        result = []
        while len(q):
            l = len(q)
            temp = []
            while l > 0:
                if zig:
                    current_node = q.popleft()
                    temp.append(current_node.val)
                    if current_node.right:
                        q.append(current_node.right)
                    if current_node.left:
                        q.append(current_node.left)
                else:
                    current_node = q.pop()
                    temp.append(current_node.val)
                    if current_node.left:
                        q.appendleft(current_node.left)
                    if current_node.right:
                        q.appendleft(current_node.right)
                l -= 1
            result.append(temp)
            zig = not zig

        return result
