
from __future__ import annotations
from collections.abc import Iterable, Iterator

test_data_odd = (3, 9, -11, 0, 7, 5, 1, -1)
test_data_even = (4, 6, 2, 0, 8, 10, 3, -2)


class Node:
    def __init__(self, data: int, next: None):
        self.data = data
        self.next = None


class SortedLinkedList:
    def __init__(self, data: Iterable[int]) -> None:
        self.head = None

        for i in reversed(sorted(data)):
            self.head = Node(i, self.head)

    def __iter__(self) -> Iterator[int]:
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self):
        return len(tuple(iter(self)))

    def __str__(self):
        return " -> ".join([str(item) for item in self])


def merge_lists(sll_one: SortedLinkedList, sll_two: SortedLinkedList):
    return SortedLinkedList(list(sll_one) + list(sll_two))


if __name__ == "__main__":
    SSL = SortedLinkedList
    print(merge_lists(SSL(test_data_even), SSL(test_data_odd)))
