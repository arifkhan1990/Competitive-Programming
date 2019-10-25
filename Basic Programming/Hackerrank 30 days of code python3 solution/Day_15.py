#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Day 15: Linked List
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/30-linked-list/problem
#

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        n = Node(data)
        if head:
            current = head
            while current.next:
                current = current.next
            current.next = n
            return head
        else:
            return n
    #Complete this method

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  