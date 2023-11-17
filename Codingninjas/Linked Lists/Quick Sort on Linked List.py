from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the class structure of the Node class:

    class Node:
        def __init__(self, data):

            self.data = data
            self.next = None

        def __del__(self):
            if(self.next):
                del self.next
                
'''

def partition(left, right):

    if left == right or left == None or right == None:
        return left

    pivot_prev = curr = left
    pivot = right

    while left != right:

        if left.data < pivot.data:
            pivot_prev = curr
            curr.data, left.data = left.data, curr.data
            curr = curr.next

        left = left.next

    curr.data, right.data = right.data, curr.data
    return pivot_prev


def sort(left, right):

    if left is None or left == right or left == right.next:
        return None
    pivot = partition(left, right)

    sort(left, pivot)

    if pivot.next:
        sort(pivot.next, right)
    else:
        return None


def quickSortLL(head):

    if head is None or head.next is None:
        return head
    
    curr = head
    while curr.next:
        curr = curr.next

    sort(head, curr)
    return head
















