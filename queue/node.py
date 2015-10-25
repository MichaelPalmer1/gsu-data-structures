# Michael Palmer
# CSCI 3230 A
# March 23, 2015
# Project 2


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self, front = None):
		self.front = front

	def insert_front(self, item):
		if not self.front:
			self.front = item
		else:
			item.next = self.front
			self.front = item

	def get_list(self):
		current = self.front
		output = ""
		while current:
			output += "%s " % current.data
			current = current.next
		return output