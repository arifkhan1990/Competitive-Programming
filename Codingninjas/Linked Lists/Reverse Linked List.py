'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def reverseLinkedList(head):
    prev, curr, newN = None, head, None
    while curr:
        newN = curr.next
        curr.next = prev
        prev = curr
        curr = newN
    return prev
    