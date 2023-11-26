def searchInLinkedList(head, k):
    while head:
        if head.data == k:
            return 1
        head = head.next
    return 0