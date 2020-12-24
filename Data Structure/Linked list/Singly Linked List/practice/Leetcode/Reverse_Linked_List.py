#                      Name : Arif Khan
#                      Judge: Leetcode
#                      University: Primeasia University
#                      problem: Reverse Linked List
#                      Difficulty: Easy
#                      Problem Link: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1205/

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node
        head = prev
        return head
