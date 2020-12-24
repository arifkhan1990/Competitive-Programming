#                      Name : Arif Khan
#                      Judge: Leetcode
#                      University: Primeasia University
#                      problem: Odd Even Linked List
#                      Difficulty: Easy
#                      Problem Link: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/
#

# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL

# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL

# Input: 2->NULL
# Output: 2->NULL

# Input: 2->1->NULL
# Output: 2->1->NULL

# Input: []
# Output: []
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        even = None
        odd = head
        temp = None
        i = 1
        curr = ListNode()

        while odd is not None and odd.next:
            if i % 2:
                if odd == head:
                    curr = odd
                    head = curr
                else:
                    curr.next = odd
                    curr = curr.next
            else:
                if i == 2:
                    even = odd
                    temp = even
                else:
                    even.next = odd
                    even = even.next
            i += 1
            odd = odd.next

        if odd is not None:
            if i % 2:
                curr.next = odd
                curr = curr.next
                if even is not None:
                    even.next = None
            else:
                if even is not None:
                    even.next = odd
                    even = even.next
                    even.next = None
                else:
                    even = odd
                    even.next = None
                    temp = even

            if temp is not None:
                curr.next = temp
            else:
                curr.next = None

        return head


# def oddEvenList(self, head: ListNode) -> ListNode:
#        if not head or not head.next: return head
#        odd=head
#        even=head.next
#        even_head=head.next
#        while even and even.next:
#            odd.next=odd.next.next
#            even.next=even.next.next
#            odd=odd.next
#            even=even.next
#        odd.next=even_head
#       return head
###
