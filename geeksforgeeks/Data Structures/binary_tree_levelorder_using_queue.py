#!/usr/bin/python

class Node:
	# A utility function to create a new node
	def __init__(self ,key):
		self.data = key
		self.left = None
		self.right = None


def levelorder_travarsal_queue(root):
	if root == None:
		return

	queue = []
	queue.append(root)
	while len(queue) > 0:
		print queue[0].data
		node = queue.pop(0)
		
		if node.left is not None:
			queue.insert(0, node.left)

		if node.right is not None:
			queue.insert(0, node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print "Level Order Traversal of binary tree is -"
levelorder_travarsal_queue(root)