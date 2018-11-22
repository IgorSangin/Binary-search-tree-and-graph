class BinTreeNode(object):
 
	def __init__(self, value):
		self.value=value
		self.left=None
		self.right=None
		
f = open("paragraph.txt", "r")
paragraph = f.read().split()
 
       
def tree_insert( tree, value):
    if tree==None:
        tree=BinTreeNode(value)
    else:
        if value < tree.value:
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
	"""Finding a word"""
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
		
 
def pre_order(tree):
	"""Output item, then follow left tree,
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
	print(tree_search(t, "tree"))	

main()