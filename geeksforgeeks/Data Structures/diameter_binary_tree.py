#!/usr/bin/python

class Node:
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def diameter_binary_tree(root):
	if root == None:
		return 0

	ldiameter = diameter_binary_tree(root.left)
	rdiameter = diameter_binary_tree(root.right)

	lheight = height(root.left)
	rheight = height(root.right)

	return max(lheight + rheight + 1, max(ldiameter, rdiameter))

def height(node):
	if node is None:
		return 0

	return max(height(node.left), height(node.right)) + 1

"""
Constructed binary tree is 
						1
					  /   \
				    2      3
			      /  \
		        4     5
"""
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print height(root)
print "Diameter of given binary tree is %d" %(diameter_binary_tree(root))