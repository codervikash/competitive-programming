"""
Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def path_sum_util(self, root, sum1, result, path):
		if root is None:
			return
		path.append(root.val)
		sum1 = sum1 - root.val
		if sum1 == 0 and root.left is None and root.right is None:
			result.append(path)
		else:
			self.path_sum_util(root.left, sum1, result, path[:])
			self.path_sum_util(root.right, sum1, result, path[:])

		return


	# @param root : root node of tree
	# @param sum1 : integer
	# @return a list of list of integers
	def pathSum(self, root, sum1):
		if root is None:
			return
		result = []
		self.path_sum_util(root, sum1, result, [])
		return result
