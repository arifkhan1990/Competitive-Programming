#                      Name : Arif Khan
#                      Judge: Leetcode
#                      University: Primeasia University
#                      problem: Remove Nth Node From End of List
#                      Difficulty: Medium
#                      Problem Link: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/


#    Input: head = [1,2,3,4,5], n = 2
#    Output: [1,2,3,5]
#    Input: head = [1], n = 1
#    Output: []
#    Input: head = [1,2], n = 1
#    Output: [1]
#    Input: head = [1,2], n = 2
#    Output: [2]

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size, temp = 0, head
        # calculate size of linked list
        while temp.next is not None:
            temp = tempp.next
            size += 1
        size = size + 1 - n

        curr = prev = head

        if size == 0:
            # if remove the first node int the list
            if curr.next is not None:
                head = curr.next
            # if list lent is 1 and remove the node
            else:
                return None

        # find the removed node and previous node
        while size != 0:
            prev, curr = curr, curr.next
            size -= 1

        # if remove node is last node at linked list
        if curr.next is None:
            prev.next = None
        else:
            prev.next = curr.next
        return head
