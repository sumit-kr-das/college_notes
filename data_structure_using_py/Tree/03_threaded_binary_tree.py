# Insertion in Threaded Binary Search Tree.
class newNode:
	def __init__(self, key):
	
		# False if left pointer points to
		# predecessor in Inorder Traversal
		self.info = key
		self.left = None
		self.right =None
		self.lthread = True
	
		# False if right pointer points to
		# successor in Inorder Traversal
		self.rthread = True

# Insert a Node in Binary Threaded Tree
def insert(root, ikey):
	
	# Searching for a Node with given value
	ptr = root
	par = None # Parent of key to be inserted
	while ptr != None:
		
		# If key already exists, return
		if ikey == (ptr.info):
			print("Duplicate Key !")
			return root

		par = ptr # Update parent pointer

		# Moving on left subtree.
		if ikey < ptr.info:
			if ptr.lthread == False:
				ptr = ptr.left
			else:
				break

		# Moving on right subtree.
		else:
			if ptr.rthread == False:
				ptr = ptr.right
			else:
				break

	# Create a new node
	tmp = newNode(ikey)

	if par == None:
		root = tmp
		tmp.left = None
		tmp.right = None
	elif ikey < (par.info):
		tmp.left = par.left
		tmp.right = par
		par.lthread = False
		par.left = tmp
	else:
		tmp.left = par
		tmp.right = par.right
		par.rthread = False
		par.right = tmp

	return root

# Returns inorder successor using rthread
def inorderSuccessor(ptr):
	
	# If rthread is set, we can quickly find
	if ptr.rthread == True:
		return ptr.right

	# Else return leftmost child of
	# right subtree
	ptr = ptr.right
	while ptr.lthread == False:
		ptr = ptr.left
	return ptr

# Printing the threaded tree
def inorder(root):
	if root == None:
		print("Tree is empty")

	# Reach leftmost node
	ptr = root
	while ptr.lthread == False:
		ptr = ptr.left

	# One by one print successors
	while ptr != None:
		print(ptr.info,end=" ")
		ptr = inorderSuccessor(ptr)

# Driver Code
if __name__ == '__main__':
	root = None

	root = insert(root, 20)
	root = insert(root, 10)
	root = insert(root, 30)
	root = insert(root, 5)
	root = insert(root, 16)
	root = insert(root, 14)
	root = insert(root, 17)
	root = insert(root, 13)

	inorder(root)
	
# This code is contributed by PranchalK
