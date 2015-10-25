# Michael Palmer
# CSCI 3230 A
# March 23, 2015
# Project 2

from node import *
from random import randint
from time import time

# Initialize variables
ll = LinkedList()
count = 0


# Return element at the front of the linked list
def front():
	return ll.front


# Add an item to the end of the queue
def enqueue(item):
	global count

	if not front():
		# Queue is empty, adding item to front
		ll.front = item
	else:
		# Queue has elements, setting current to the first element
		current = front()

		# Find the end of the queue
		while current.next:
			current = current.next

		# Add item to the end
		current.next = item

	# Increase size of queue
	count += 1

	# Display execution message
	print "Enqueued item %d (%d)" % (item.data, count)


# Remove an item from the front of the queue
def dequeue():
	global count

	# Verify the queue has elements
	assert front()

	# Update the first element
	ll.front = front().next

	# Decrease size of queue
	count -= 1

	# Display execution message
	print "Executed dequeue()"


# Get the size of the queue
def size():
	global count
	return count


# Run a queue
def queue(elements, do_dequeue=True, build_time=False, show_contents=True):
	global count
	start = None

	# Output message describing queue size
	print "Creating queue with %d elements" % elements

	# Save execution start time
	if build_time:
		start = time()

	# Create the queue
	for _ in range(elements):
		# Add new item with random value between 1 and 10
		new_item = Node(randint(1, 10))

		# Enqueue the item
		enqueue(new_item)

		# Print the contents of the queue
		if show_contents:
			print "Queue Content: %s" % ll.get_list()

	# Output queue statistics
	if show_contents:
		print "-------------------------------------------"
		print "Final Content of Queue: %s" % ll.get_list()
		print "Size: %d elements" % size()
		print "-------------------------------------------"

	# Execute dequeue()
	if do_dequeue:
		for _ in range(elements):
			dequeue()

			# Show queue contents
			if show_contents:
				print "Queue Content: %s" % ll.get_list()

	# Output execution time
	if build_time:
		duration = time() - start
		if duration >= 1:
			print "Build Time: %1.3f sec" % duration
		else:
			print "Build Time: %1.3f ms" % (duration * 1000)


# Create a queue with the following settings:
# Num of elements: 20
# Execute dequeue: Yes
# Save build time: No
# Output contents: Yes
queue(20)

# Wait to continue
print ""
raw_input("Press enter to create a queue with 10,000 elements...")

# Create a queue with the following settings:
# Num of elements: 10,000
# Execute dequeue: No
# Save build time: Yes
# Output contents: No
queue(10000, False, True, False)