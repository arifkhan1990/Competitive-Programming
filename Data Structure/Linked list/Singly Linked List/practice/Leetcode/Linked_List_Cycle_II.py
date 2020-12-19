#                      Name : Arif Khan
#                      Judge: Leetcode
#                      University: Primeasia University
#                      problem: Linked List Cycle II
#                      Difficulty: Medium
#                      Problem Link: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/
#


class Solution:
    # Input: head = [3,2,0,-4], pos = 1
    # Output: tail connects to node index 1
    # Explanation: There is a cycle in the linked list, where tail connects to the second node.

    # Input: head = [3,2,0,-4], pos = 0
    # Output: tail connects to node index 0
    # Explanation: There is a cycle in the linked list, where tail connects to the first node.

    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        d = {}
        while fast:
            if fast in d.keys():
                return fast
            d[fast] = None
            fast = fast.next
        return None
