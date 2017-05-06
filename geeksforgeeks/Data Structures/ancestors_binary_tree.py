# A Binary Tree node
class Node:

	def __init__(self, data):
		self.data = data 
		self.left = None
		self.right = None

# If target is present in tree, then prints the ancestors
# and returns true, otherwise returns false
def print_ancestors(root, target):
	if root == None:
		return False

	if root.data == target:
		return True

	if(printAncestors(root.left, target) or
		printAncestors(root.right, target)):
		print root.data
		return True

	return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
 
print_ancestors(root, 7)