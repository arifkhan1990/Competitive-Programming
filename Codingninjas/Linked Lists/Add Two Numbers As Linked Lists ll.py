from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

# Following is the linked list node structure:
class Node:
    def __init__(self, data):
        
        self.data = data
        self.next = None

def reverse_list(head):
    prev = None
    curr = head
    nextN = None

    while curr:
        nextN = curr.next
        curr.next = prev
        prev = curr
        curr = nextN
    return prev


def addTwoLists(first, second):
    first = reverse_list(first)
    second = reverse_list(second)

    c = 0
    head = None
    prev = None
    sm = None

    while first or second or c == 1:
        newV = c
        if first:
            newV += first.data
        if second:
            newV += second.data

        c = newV//10
        newV %= 10

        newN = Node(newV)
        newN.next = sm
        sm = newN

        if first:
            first = first.next
        if second:
            second = second.next
    return sm

# Taking input.
def takeInput():

    firstList = None
    secondList = None

    arr = list(map(int, stdin.readline().strip().split(" ")))
    if(arr[0] != -1):

        firstList = Node(arr[0])
        last = firstList
        for data in arr[1:]:

            if(data == -1):
                break

            last.next = Node(data)
            last = last.next

    arr = list(map(int, stdin.readline().strip().split(" ")))
    if(arr[0] != -1):

        secondList = Node(arr[0])
        last = secondList
        for data in arr[1:]:

            if(data == -1):
                break

            last.next = Node(data)
            last = last.next

        return firstList, secondList

# Function to print the node values of the linked list.
def printLinkedList(head):

    while head:
        print(head.data, end=' ')
        head = head.next

    print(-1)

# Main.
T = int(stdin.readline().strip())
for i in range(T):
    first, second = takeInput()
    answerList = addTwoLists(first, second)
    printLinkedList(answerList)