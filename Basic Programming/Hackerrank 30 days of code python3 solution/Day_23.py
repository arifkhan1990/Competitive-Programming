#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Day 23: BST Level-Order Traversal
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/30-binary-trees/problem
#

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self, root):
        Q = []
        Q.append(root)
        while (Q):
            t = Q[0]
            print(t.data,end=' ')
            if t.left is not None:
                Q.append(t.left)
            if t.right is not None:
                Q.append(t.right)
            Q.pop(0)

T=int(input())
