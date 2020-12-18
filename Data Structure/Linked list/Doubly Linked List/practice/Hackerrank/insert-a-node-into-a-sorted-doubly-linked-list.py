#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Inserting a Node Into a Sorted Doubly Linked List
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?isFullScreen=false
#


import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)
    if head is None:
        head = new_node
    elif head.data > data:
        new_node.next, head.prev = head, new_node
        head = new_node

    else:
        temp = head
        while temp.next is not None and temp.data < data:
            temp = temp.next

        if temp.next is None and temp.data < data:
            temp.next, new_node.prev = new_node, temp
        else:
            previous = temp.prev
            previous.next = new_node
            new_node.prev = previous
            new_node.next = temp
            temp.prev = new_node
    return head

    # recursion process
    # def sortedInsert(head, data):
    #    new_node = DoublyLinkedListNode(data)
    #    if head is None:
    #        head = new_node
    #    elif data < head.data:
    #       new_node.next , head.prev = head, new_node
    #        head = new_node
    #    else:
    #        new_node = sortedInsert(head.next, data)
    #        head.next, new_node.prev = new_node, head
    #    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
