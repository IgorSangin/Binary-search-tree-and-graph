"""Class BinTreeNode, __init__ method
	and function tree_insert
	written by Diana Hintea.
	Availability: http://moodle.coventry.ac.uk"""


class BinTreeNode(object):
	"""A class to hold a node in a binary search tree"""

	def __init__(self, value):
		"""Instantiation method
		takes value which we provide for the node
		and assigns left and right children
		of the node to None.
		Frequency keeps track of the frequency of particular word."""
		
		self.frequency = 0
		self.value=value
		self.left=None
		self.right=None
		
f = open("paragraph.txt", "r")
paragraph = f.read().split() # split the paragraph to list of words
f.close()
 
       
def tree_insert( tree, value):
	"""Function to insert a node into a tree,
	tree is a node,
	value is the word we insert from paragraph"""

	if tree==None:
		tree=BinTreeNode(value)
	else:
		if value == tree.value:
			tree.frequency = tree.frequency + 1
		elif value < tree.value:
			if tree.left==None:
				tree.left=BinTreeNode(value)
			else:
				tree_insert(tree.left,value)
		else:
			if tree.right==None:
				tree.right=BinTreeNode(value)
			else:
				tree_insert(tree.right,value)
	return tree


def tree_search(tree, target):
	"""Finding a word
	target is a word we want to find"""
	
	try:
		r = tree
		while r != None:
			print(r.value) # to print the path to the word we are looking for
			if r.value == target:
				return "Yes"
			elif r.value > target:
				r = r.left
			else:
				r = r.right
		return "No"
	except TypeError:
		print("Please specify a word, not a number.")


def pre_order(tree):
	"""Travels tree in pre order:
	output item, then follow left tree,
	then right tree"""

	print(tree.value)
	if tree.left != None:
		pre_order(tree.left)
	if tree.right != None:
		pre_order(tree.right)
		
		
				
		
		

def main():
	"""Main function to call other functions"""
	t = None
	for word in paragraph:
		word = word.lower()
		t = tree_insert(t, word)

	print("Let's travel through binary search tree in pre order:\n")
	pre_order(t)
	print("\nNow let's search the word and output it's path:\n")
	print(tree_search(t, "binary"))	

main()