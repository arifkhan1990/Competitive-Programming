#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Delete duplicate-value nodes from a sorted linked list
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem
#

import math
import os
import re
import random
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data, self.next = data, None


class SinglyLinkedList:
    def __init__(self):
        self.head, self.tail = None, None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next

        if node:
            fptr.write(sep)


def removeDuplicates(head):
    if head is None:
        return head
    node = head
    while node.next is not None:
        temp = node.next
        while temp and temp.data != node.data:
            temp = temp.next
        node.next, node = temp, node.next
    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = removeDuplicates(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
