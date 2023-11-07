from os import *
from sys import *
from collections import *
from math import *

# List Node Class.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_list(head):
    prev = None
    curr = head
    newN = None
    while curr:
        newN = curr.next
        curr.next = prev
        prev = curr
        curr = newN
    return prev

def lastAppearance(head):
    dmm = Node(-1)
    dmm.next = head
    dmm.next = reverse_list(head)
    visited = set()
    curr = dmm
    nextN = None

    while curr and curr.next:
        nextN = curr.next

        if visited.__contains__(nextN.data):
            curr.next = nextN.next
        else:
            visited.add(nextN.data)
            curr = nextN
    dmm.next = reverse_list(dmm.next)
    return dmm.next