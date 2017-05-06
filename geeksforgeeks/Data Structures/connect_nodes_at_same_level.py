"""
Write a function to connect all the adjacent nodes at the same level in a binary tree.

Initially, all the nextRight pointers point to garbage values. Your function should set these pointers to point next right for each node.
"""


class Node:
	# Constructor to create a new node
	def __init__(self, data, next_right = None):
		self.data = data 
		self.left = None
		self.right = None
		self.next_right = next_right

def connected_nodes(root):
	if root == None:
		return

	queue = []
	level = 0
	queue.append(root)
	queue.append(level)
	while len(queue) > 0:
		node = queue.pop(0)
		level = queue.pop(0)
		if(len(queue) > 1):
			if queue[1] == level:
				node.next_right = queue[0]
		
		if node.left is not None:
			queue.append(node.left)
			queue.append(level + 1)

		if node.right is not None:
			queue.append(node.right)
			queue.append(level + 1)
"""
Construct the following tree

						26
					 /    \
				    10     3
				  /    \    \
			     4      6    3
"""
 
root = Node(26)
root.right = Node(3)
root.right.right  = Node(3)
root.left = Node(10)
root.left.left = Node(4)
root.left.right = Node(6)
connected_nodes(root)

# test to verify nodes are connected
print root.left.left.next_right
print root.left.right
 
		