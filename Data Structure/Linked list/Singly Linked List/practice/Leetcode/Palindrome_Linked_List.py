#                      Name : Arif Khan
#                      Judge: Leetcode
#                      University: Primeasia University
#                      problem: Palindrome Linked List
#                      Difficulty: Easy
#                      Problem Link: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1209/
#


# Input: 1->2->2->1
# Output: true

# Input: 1->2
# Output: false

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slow = fast = curr = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        stack = [slow.val]
        while slow.next:
            slow = slow.next
            stack.append(slow.val)

        while stack:
            if stack.pop() != curr.val:
                return False
            curr = curr.next

        return True
