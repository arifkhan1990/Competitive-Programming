#                      Name : Arif Khan
#                      Judge: Leetcode
#                      University: Primeasia University
#                      problem: Intersection of Two Linked Lists
#                      Difficulty: Medium
#                      Problem Link: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/
#


class Solution:
    # Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    # Output: Reference of the node with value = 8
    # Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
    # From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A;
    # There are 3 nodes before the intersected node in B.
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curr1, curr2 = headA, headB
        while curr1 != curr2:
            if curr1 is None:
                curr1 = headB
            else:
                curr1 = curr1.next

            if curr2 is None:
                curr2 = headA
            else:
                curr2 = curr2.next
        return curr1
