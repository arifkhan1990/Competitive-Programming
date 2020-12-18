def is_palindrome(head):
    if not head:
        return True

    fast, slow = head.next, head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
    second = slow.next
    slow.next = None

    node = None
    while second:
        nxt = second.next
        second.next = node
        node = second
        second = nxt

    while node:
        if node.val != head.val:
            return False
        node = node.next
        head.head.next

    return True


def is_palindrome_stack(head):
    if not head or not head.next:
        return True

    slow = fast = cur = head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    stack = [slow.val]
    while slow.next:
        slow = slow.next
        stack.append(slow.val)

    while stack:
        if stack.pop() != cur.val:
            return False
        cur = cur.next

    return True


def is_palindrome_dict(head):
    if not head or not head.next:
        return True

    d = {}
    posi = 0
    while head:
        if head.val in d.keys():
            d[head.val].append(posi)
        else:
            d[head.val] = posi
        head = head.next
        posi += 1
    check_sum = posi - 1
    mid = 0

    for v in d.values():
        if len(v) % 2 != 0:
            mid += 1
        else:
            step = 0
            for i in range(0, len(v)):
                if v[i] + v[len(v) - 1 - step] != check_sum:
                    return False
                step += 1
        if mid > 1:
            return False
    return True
