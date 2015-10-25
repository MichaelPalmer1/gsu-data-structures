from random import randint


class Tree:
	# Constructor
	def __init__(self, value, parent=None):
		self.value = value
		self.parent = parent
		self.left = None
		self.right = None

		while parent is not None:
			parent = parent.parent

	def root(self):
		root = self
		while root.parent is not None:
			root = root.parent
		return root


class BST(Tree):
	# Add node to tree
	def add(self, value):
		current = self.root()

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

	# Sort using in-order sort
	def sort_in_order(self):
		current = self.root()
		visited = []
		sorted_list = []

		# Find maximum node (bottom right)
		maximum = self.root()
		while maximum.right is not None:
			maximum = maximum.right

		# Go to minimum node (bottom left)
		while current.left is not None:
			current = current.left

		# Parse through the tree
		while current is not maximum:
			if current not in visited:
				# Node has not yet been visited, adding to visited list
				visited.append(current)

				# Add value to sorted list
				sorted_list.append(current.value)
			else:
				# Node has been visited already, going to parent
				current = current.parent
				continue

			if current.right is not None:
				# Right child exists, going to that node
				current = current.right

				# Go to bottom left child (minimum value)
				while current.left is not None:
					current = current.left

			else:
				# No right child, going to parent
				current = current.parent

		# Maximum node is added to the list within the loop, doing that here
		sorted_list.append(maximum.value)

		# Return sorted list
		return sorted_list


class Heap(Tree):
	count = 0
	rows = 0
	arr = []

	def __init__(self):
		Tree.__init__(self, None, None)

	def swap(self, array, a, b):
		array[a], array[b] = array[b], array[a]

	def build_heap(self, a):
		self.count = len(a)
		start = (self.count - 2) / 2

		while start >= 0:
			self.sort(a, start, self.count - 1)
			start -= 1

		end = self.count - 1

		while end > 0:
			self.swap(a, end, 0)
			self.sort(a, 0, end - 1)
			end -= 1

	def sort(self, a, start, end):
		root = start

		while root * 2 + 1 <= end:
			child = root * 2 + 1
			if (child + 1) <= end and a[child] < a[child + 1]:
				child += 1

			if child <= end and a[root] < a[child]:
				self.swap(a, root, child)
				root = child
			else:
				break

	def traverse(self, i):
		current = self.root()
		print("-----")
		parent = 0
		n = 0
		up = 0
		down = 1
		left = 1
		right = 0
		while n < i:
			current = current.left
			n += 1
			for _ in range(down):
				if left > 0:
					current = current.left
					left += 1


			n += 1

		while n > 0:
			if divmod(n, 2)[1] is 1 and current.left is not None:
				print("Left from %d to %d" % (current.value, current.left.value))
				print("Parent: %d (%d)" % (parent, self.arr[parent]))
				current = current.left
				n -= 2
			elif divmod(n, 2)[1] is 0 and current.right is not None:
				print("Right from %d to %d" % (current.value, current.right.value))
				current = current.right
				n -= 2

		print(current.value)

	# Add node to tree
	def add(self, value):
		current = self.root()
		self.arr.append(value)

		# Update number of elements and rows
		self.root().count += 1
		while not self.root().count in range(pow(2, self.root().rows), pow(2, self.root().rows + 1)):
			self.root().rows += 1

		print("Rows: %d, Count: %d - [%d,%d]" % (self.root().rows, self.root().count, pow(2, self.root().rows), pow(2, self.root().rows + 1) - 1))
		first = pow(2, self.root().rows)
		last = pow(2, self.root().rows + 1) - 1

		# number vs. row
		if self.root().count is first:
			while current.left is not None:
				# print("Parent is %d" % ((len(self.arr) - 1) / 2))
				print("Left from %d to %d" % (current.value, current.left.value))
				current = current.left
			print("Bottom left: %d" % value)
			current.left = Heap(value, current)
			return
		elif self.root().count is last:
			while current.right is not None:
				# print("Parent is %d" % ((len(self.arr) - 1) / 2))
				print("Right from %d to %d" % (current.value, current.right.value))
				current = current.right
			print("Bottom right: %d" % value)
			current.right = Heap(value, current)
			return
		else:
			for _ in range(self.root().rows - 2):
				if current is None or current.left is None:
					break

				current = current.left
				print("Going left from %s to %s" % (current.value, current.left.value))

			# while current is not None:
			# 	if current.parent is None:
			# 		print("Top level")
			# 		if current.left is None and current.right is None:
			# 			print("First left child: %d" % value)
			# 			current.left = Heap(value, current)
			# 			break
			# 		elif current.left is not None and current.right is None:
			# 			print("First right child: %d" % value)
			# 			current.right = Heap(value, current)
			# 			break
			# 		else:
			# 			current = current.left
			# 	else:
			# 		if current.left is None and current.right is None:
			# 			print("Left child: %d" % value)
			# 			current.left = Heap(value, current)
			# 			break
			# 		elif current.left is not None and current.right is None:
			# 			print("Right child: %d" % value)
			# 			current.right = Heap(value, current)
			# 			break
			# 		elif current.left is not None and current.right is not None:
			# 			if current.left.left is None and current.left.right is None:
			# 				current = current.left
			# 			elif current.left.left is not None and current.left.right is None:
			# 				current = current.left
			# 			else:
			# 				current = current.parent.right

			while current is not None:
				if current.parent is None:
					if current.left.left is None or current.left.right is None:
						print("Go left from %d to %d" % (current.value, current.left.value))
						current = current.left
					elif current.left.left is not None and current.left.right is not None:
						print("Go right from %d to %d" % (current.value, current.right.value))
						current = current.right
					elif current.right.left is None or current.right.right is None:
						print("Go right from %d to %d" % (current.value, current.right.value))
						current = current.right
					else:
						print("ELSE WHILE")
						break
				else:
					if divmod(self.root().count, 2)[1] is 0:
						print("Left child: %d" % value)
						current.left = Heap(value, self)
						break
					else:
						print("Right child: %d" % value)
						current.right = Heap(value, current)
						break


"""""""""""""""""""""
BST Test Program
"""""""""""""""""""""
print("Binary Search Tree -- Sorted using in-order traversal")
print("------------")

tree = BST(randint(1, 100))
nums = []

# Create a list (with 30 - 50 elements) of random integers (between 1 - 100)
# First element was added with initializer
for a in range(randint(29, 39)):
	nums.append(randint(1, 100))

# Output list size
print("List Size: %d elements" % len(nums))

# Output original list prior to BST sort
print("Unsorted: %s" % nums)

# Add nodes to the tree
for x in nums:
	tree.add(x)

# Sort the tree using in-order sorting and output the result
print("Sorted: %s" % tree.sort_in_order())

# Create a list (with 30 - 50 elements) of random integers (between 1 - 100)
heap_nums = []
for b in range(randint(30, 40)):
	heap_nums.append(randint(1, 100))

print("\nHeap Sort:")
print("------------")

# Output list size
print("List Size: %d elements" % len(heap_nums))

# Output original list prior to BST sort
print("Unsorted: %s" % heap_nums)
heap = Heap()
heap.build_heap(heap_nums)
print("Sorted: %s" % heap_nums)

"""
print("\t\t\t    3")
print("\t    .______________/ \______________.")
print("\t    8\t\t\t\t    15")
print("    .______/ \______.\t\t    .______/  \______.")
print("    7\t\t    4\t\t    10\t\t    18")
print(".__/ \__.\t.__/ \__.\t.__/  \__.\t.__/  \__.")
print("1\t2\t3\t5\t20\t15\t17\t19")
							3
			.______________/ \______________.
			8                               15
	.______/ \______.               .______/  \______.
	7               4               10               18
.__/ \__.       .__/ \__.       .__/  \__.       .__/  \__.
1       2       3       5       20       15      17       19
"""
