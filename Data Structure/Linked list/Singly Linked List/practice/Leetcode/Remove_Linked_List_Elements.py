#                      Name : Arif Khan
#                      Judge: Leetcode
#                      University: Primeasia University
#                      problem: Remove Linked List Elements
#                      Difficulty: Easy
#                      Problem Link: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/
#

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev, curr = None, head
        while curr:
            if val == curr.val:
                if prev is None:
                    if curr.next is not None:
                        head = curr.next
                    else:
                        head = None
                elif curr.next is None:
                    prev.next = None
                else:
                    prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head
