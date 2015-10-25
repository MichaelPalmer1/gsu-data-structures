from random import randint

class Tree:
	# Constructor
	def __init__(self, value, parent=None):
		self.value = value
		self.parent = parent
		self.left = None
		self.right = None


class BST(Tree):
	PRE_ORDER = 0
	IN_ORDER = 1
	POST_ORDER = 2

	# Add node to tree
	def add(self, value):
		current = self
		while current.parent is not None:
			current = current.parent

		while True:
			# Create left children
			if value < current.value:
				if current.left is None:
					# Create new node in left child and finish
					current.left = BST(value, current)
					break
				else:
					# Go to left child
					current = current.left

			# Create right children
			else:
				if current.right is None:
					# Create new node in right child and finish
					current.right = BST(value, current)
					break
				else:
					# Go to right child
					current = current.right

	def sort(self, order, node=-1, sorted=[]):
		if node is -1:
			node = self
			sorted = []
		elif node is None:
			return sorted

		# Pre-Order
		if order is self.PRE_ORDER:
			sorted.append(node.value)

		sorted = self.sort(order, node.left, sorted)

		# In-Order
		if order is self.IN_ORDER:
			sorted.append(node.value)

		sorted = self.sort(order, node.right, sorted)

		# Post-Order
		if order is self.POST_ORDER:
			sorted.append(node.value)

		return sorted


class Heap(Tree):
	count = 0

	# Constructor
	def __init__(self, a):
		Tree.__init__(self, None, None)
		self.array = a
		self.count = len(self.array)

	# Swap elements
	def swap(self, a, b):
		self.array[a], self.array[b] = self.array[b], self.array[a]

	# Create heap
	def build_heap(self):
		# Sort the start of the list
		start = (self.count - 2) / 2
		while start >= 0:
			self.sort(start, self.count - 1)
			start -= 1

		# Perform remove min operation and sort the end of the list
		end = self.count - 1
		while end > 0:
			self.swap(end, 0)
			self.sort(0, end - 1)
			end -= 1

	# Sort heap
	def sort(self, start, end):
		# Start sort at root
		root = start

		# While element is within the list
		while (2 * root) + 1 <= end:
			child = (2 * root) + 1
			if (child + 1) <= end and self.array[child] < self.array[child + 1]:
				child += 1

			if child <= end and self.array[root] < self.array[child]:
				# Swap the elements
				self.swap(root, child)
				root = child
			else:
				break

"""""""""""""""""""""
Create List
"""""""""""""""""""""
print("----------------------------------------------")
print("List Statistics:")
print("----------------------------------------------")

# Create a list (with 30 - 50 elements) of random integers (between 1 - 100)
nums = []
length = randint(30, 50)
while len(nums) < length:
	nums.append(randint(1, 100))

# Output list size
print("Size: %d elements\n" % length)

# Output original list prior to BST sort
print("Unsorted:\n%s\n" % nums)

"""""""""""""""""""""
Binary Search Tree
"""""""""""""""""""""
print("----------------------------------------------")
print("Binary Search Tree:")
print("----------------------------------------------")

# Create root node of BST
tree = BST(nums[0])

# Add remaining nodes to the BST
for x in nums[1:]:
	tree.add(x)

# Output using pre-order traversal
print("Pre-Order:\n%s\n" % tree.sort(tree.PRE_ORDER))

# Output using in-order traversal
print("In-Order:\n%s\n" % tree.sort(tree.IN_ORDER))

# Output using post-order traversal
print("Post-Order:\n%s\n" % tree.sort(tree.POST_ORDER))

"""""""""""""""""""""
Heap Sort
"""""""""""""""""""""
print("----------------------------------------------")
print("Heap:")
print("----------------------------------------------")

# Create heap and sort it
heap = Heap(nums)
heap.build_heap()

# Output sorted list
print("Heap Sort:\n%s" % nums)
