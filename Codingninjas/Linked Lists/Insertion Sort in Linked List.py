from os import *
from sys import *
from collections import *
from math import *

'''
	# Linked List Node class for reference

	class Node:
	    def __init__(self, data):
	        self.data = data
	        self.next = None
'''
def sortedInsert(head, newN):
	curr = None
	if head == None or head.data >= newN.data:
		newN.next = head
		head = newN
	else:
		curr = head
		while curr.next != None and curr.next.data < newN.data:
			curr = curr.next
		
		newN.next = curr.next
		curr.next = newN
	return head
	
def insertionSortLL(head):
	h = None
	curr = head
	
	while curr != None:
		nt = curr.next
		h = sortedInsert(h, curr)
		curr = nt
	head = h
	return head
