#                      Name : Arif Khan
#                      Judge: Leetcode
#                      University: Primeasia University
#                      problem: Merge Two Sorted Lists
#                      Difficulty: Easy
#                      Problem Link: https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1227/
#


# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Input: l1 = [1,2,4], l2 = []
# Output: [1,2,4]

# Input: l1 = [], l2 = [1,3,4]
# Output: [1,3,4]

# Input: l1 = [], l2 = []
# Output: []
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = ListNode()
        if l1 is None and l2 is None:
            return
        if l1 is None:
            head = l2
        elif l2 is None:
            head = l1
        else:
            i = 0
            while l1 or l2:
                if i == 0:
                    if l1.val < l2.val:
                        curr = l1
                        l1 = l1.next
                    else:
                        curr = l2
                        l2 = l2.next
                    head = curr
                if l2 is None:
                    curr.next = l1
                    l1 = l1.next
                elif l1 is None:
                    curr.next = l2
                    l2 = l2.next
                else:
                    if l1.val < l2.val:
                        curr.next = l1
                        l1 = l1.next
                    else:
                        curr.next = l2
                        l2 = l2.next
                curr = curr.next

                i = 1
        return head
