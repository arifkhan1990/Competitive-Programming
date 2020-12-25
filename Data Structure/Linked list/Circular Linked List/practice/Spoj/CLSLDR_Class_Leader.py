
#                      Name : Arif Khan
#                      Judge: SPOJ
#                      University: Primeasia University
#                      problem: CLSLDR - Class Leader
#                      Difficulty: Easy
#                      Problem Link: https://www.spoj.com/problems/CLSLDR/
#

# this solution is give TLE
from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None


class ListNode:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            if node == self.head:
                break

    def __repr__(self):
        return "->".join(str(item) for item in iter(self))

    def __len__(self):
        return len(tuple(iter(self)))

    def insert(self, data: Any, index: int) -> None:
        if index < 0 and index > len(self):
            return
        node = Node(data)

        if self.head is None:
            node.next = node
            self.head = self.tail = node
        elif index == 0:
            node.next = self.head
            self.head = self.tail = node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            node.next = temp.next
            temp.next = node

            if index == len(self) - 1:
                self.tail = node

    def delete(self, index: int):
        if not 0 <= index < len(self):
            return

        if self.head == self.tail:
            self.head = self.tail = None
        elif index == 0:
            self.tail.next - self.tail.next.next
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next

            temp.next = temp.next.next
            if index == len(self) - 1:
                self.tail = temp

    def delete_node(self, idx1: int, idx2: int):
        curr = None
        del_node = self.head
        i = 1
        while del_node != curr:
            if i < idx1:
                del_node = del_node.next
            else:
                j = 1
                while j < idx2:
                    del_node = del_node.next
                    if j == idx2-1:
                        curr = del_node.next
                        del_node.next = curr.next
                    j += 1
            i += 1
        print(del_node.data)

    def print_list(self):
        print(self)


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n, m, o = map(int, input().split())
        node = ListNode()
        for i in range(1, n+1):
            node.insert(i, i-1)
        node.delete_node(m, o)
