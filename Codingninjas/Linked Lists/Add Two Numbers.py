class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.


def addTwoNumbers(head1: Node, head2: Node) -> Node:
    # Write your code here.
    ans = Node(0)
    curr = ans
    carry = 0
    
    while head1 or head2:
        s = 0
        if head1:
            s += head1.data
        if head2:
            s += head2.data
        
        s += carry
        curr.next = Node(s%10)
        curr = curr.next
        carry = s//10

        if head1:
            head1 = head1.next
        if head2:
            head2 = head2.next
    if carry:
        curr.next = Node(carry)
    ans = ans.next
    return ans
