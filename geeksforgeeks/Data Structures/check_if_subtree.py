# Given two binary trees, check if the first tree is subtree of the second one.

# A subtree of a tree T is a tree S consisting of a node in T and all of its descendants in T. 
# The subtree corresponding to the root node is the entire tree; the subtree corresponding to any other node is called a proper subtree.

class Node:
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data 
		self.left = None
		self.right = None

def are_identical(root1, root2):
	if root1 is None and root2 is None:
		return True

	if root1 is None or root2 is None:
		return False

	return (root1.data == root2.data and
		are_identical(root1.left, root2.left) and
		are_identical(root1.right, root2.right))
		

def is_subtree(t, s):
	if t == None or s == None:
		return True

	if(are_identical(t, s)):
		return True

	return (is_subtree(t.left, s) or is_subtree(t.right, s))


# Driver program to test above function
 
""" TREE 1
	Construct the following tree

						26
					 /    \
				    10     3
				  /    \    \
			     4      6    3
			     \
				  30
		"""
 
T = Node(26)
T.right = Node(3)
T.right.right  = Node(3)
T.left = Node(10)
T.left.left = Node(4)
T.left.left.right = Node(30)
T.left.right = Node(6)
 
""" TREE 2
	Construct the following tree
				  10
				/    \
			   4      6
			    \
				30
		"""
S = Node(10)
S.right = Node(6)
S.left = Node(4)
S.left.right = Node(30)
 
if is_subtree(T, S):
		print "Tree 2 is subtree of Tree 1"
else :
		print "Tree 2 is not a subtree of Tree 1"
		