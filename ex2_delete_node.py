class BinTreeNode(object):
	def __init__(self, value, parent=None):
		self.value=value
		self.parent=parent
		self.left=None
		self.right=None
		
		
		
def tree_insert( tree, item):
	"""insert value into a tree
	tree is a node
	item is value being inserted"""
	if tree==None:
		tree=BinTreeNode(item)
	else:
		if item < tree.value:
			if tree.left==None:
				tree.left=BinTreeNode(item,tree)
			else:
				tree_insert(tree.left,item)
		else:
			if tree.right==None:
				tree.right=BinTreeNode(item,tree)
			else:
				tree_insert(tree.right,item)
	return tree

def tree_search(tree, target):
	"""searches the value
	tree is a node
	target is a value we search for"""
	r = tree
	while r != None:
		if r.value == target:
			return r
		elif r.value > target:
			r = r.left
		else:
			r = r.right
	return False


def in_order(tree):
	if(tree.left!=None):
		in_order(tree.left)
	print (tree.value)
	if(tree.right!=None):
		in_order(tree.right)
		
		
def count_children(n):
	count = 0
	if n.left != None:
		count = count+1
	if n.right != None:
		count = count+1
	return count

def find_min(node):
	"""find minimum value in right subtree"""
	while node.left != None:
		node = node.left
	return node

def delete_node(value):
	node = tree_search(t, value)
	if node:
		parent = node.parent
		childrenNr = count_children(node)
		# case of 0 children:
		if childrenNr == 0:
			if parent.right == node:
				parent.right = None
			else:
				parent.left = None
			del node
		# case of 1 child:
		elif childrenNr == 1:
			if node.right != None:
				child = node.right
				if parent.right == node:
					parent.right = child
				else:
					parent.left = child
			else:
				child = node.left
				if parent.right == node:
					parent.right = child
				else:
					parent.left = child
			del node
		#case of 2 children:
		else:
			minimum = find_min(node.right)
			node.value = minimum.value
			parent = minimum.parent
			if parent.left == minimum:
				parent.left = None
			else:
				parent.right = None
			

				
	else:
		print("Node doesn't exist")
			
		



t = BinTreeNode(50)
tree_insert(t,65)
tree_insert(t,30)
tree_insert(t,70)
tree_insert(t,67)
tree_insert(t,72)
tree_insert(t,66)
tree_insert(t,75)
tree_insert(t,40)
tree_insert(t,20)
tree_insert(t,10)
tree_insert(t,45)
tree_insert(t,12)
tree_insert(t,5)
tree_insert(t,43)
tree_insert(t,25)
tree_insert(t,35)
tree_insert(t,31)

delete_node(70)
in_order(t)