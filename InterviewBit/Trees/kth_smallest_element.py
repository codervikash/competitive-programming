"""
Given a binary search tree, write a function to find the kth smallest element in the tree.

Example :

Input :
  2
 / \
1   3

and k = 2

Return : 2

As 2 is the second smallest element in the tree.
 NOTE : You may assume 1 <= k <= Total number of nodes in BST
 """

 # Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    # @param root : root node of tree
    # @param k : integer
    # @return an integer
    def kthsmallest(self, root, k):
        count = 0
        stack = deque()
        current_element = root
        done = False
        while not done:
            if current_element is not None:
                stack.appendleft(current_element)
                current_element = current_element.left
            else:
                if stack:
                    current_element = stack.popleft()
                    count += 1
                    if count == k:
                        return current_element.val
                    current_element = current_element.right
                else:
                    done = True
        return
