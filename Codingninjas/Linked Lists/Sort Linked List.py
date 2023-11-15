from os import *
from sys import *
from collections import *
from math import *

'''

  ---- Node class for reference-----
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = none
    
    def __del__(self):
        if(self.next):
            del self.next

'''

def sortedMerge(left, right):
  result = None
  if left == None:
    return right
  
  if right == None:
    return left
  
  if left.data <= right.data:
    result = left
    result.next = sortedMerge(left.next, right)
  else:
    result = right
    result.next = sortedMerge(left, right.next)
  
  return result

def getMiddle(head):
  if head == None:
    return head
  
  slow, fast = head, head

  while fast.next != None and fast.next.next != None:
    slow = slow.next
    fast = fast.next.next
  
  return slow

def sortLL(head):
  if head == None or head.next == None:
    return head

  mid = getMiddle(head)
  nextmid = mid.next

  mid.next = None
  left = sortLL(head)
  right = sortLL(nextmid)

  sortedList = sortedMerge(left, right)

  return sortedList
