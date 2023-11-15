from math import *
from collections import *
from sys import *
from os import *

import sys
from sys import stdin

# Following is the linked list node structure:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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

def sortTwoLists(first, second):
  return sortedMerge(first, second)


def ll(arr):
    
    if len(arr)==0:
        return None
    
    head = Node(arr[0])
    last = head
    
    for data in arr[1:]:
        
        last.next = Node(data)
        last = last.next
        
    return head

def printll(head):
    
    while head:
        
        print(head.data, end=' ')
        
        head = head.next
        
    print(-1)

    

t = int(sys.stdin.readline().strip())

for i in range(t):
    
    arr1=list(map(int, sys.stdin.readline().strip().split(" ")))
    arr2=list(map(int, sys.stdin.readline().strip().split(" ")))
    
    l1 = ll(arr1[:-1])
    l2 = ll(arr2[:-1])
    
    l = sortTwoLists(l1, l2)
    
    printll(l)

