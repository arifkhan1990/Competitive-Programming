from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next
            if node == self.head:
                break

    def __len__(self):
        return len(tuple(iter(self)))

    def __repr__(self):
        return "->".join(str(item) for item in iter(self))

    def insert_head(self, data: Any) -> None:
        self.insert_nth(0, data)

    def insert_tail(self, data: Any) -> None:
        self.insert_nth(len(self), data)

    def insert_nth(self, idx: int, data: Any) -> None:
        if idx < 0 or idx > len(self):
            raise IndexError('List out of range.')
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.tail = self.head = new_node
        elif idx == 0:
            new_node.next = self.head
            self.head = self.tail.next = new_node
        else:
            temp = self.head
            for _ in range(idx - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

            if idx == len(self) - 1:
                self.tail = new_node

    def print_list(self):
        print(self)

    def delete_head(self):
        return print(self.delete_nth(0))

    def delete_tail(self):
        return print(self.delete_nth(len(self) - 1))

    def delete_nth(self, idx: int = 0):
        if not 0 <= idx < len(self):
            raise IndexError("List out of range.")
        delete_node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        elif idx == 0:
            self.tail.next = self.tail.next.next
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(idx - 1):
                temp = temp.next
            delete_node = temp.next
            temp.next = temp.next.next
            if idx == len(self) - 1:
                self.tail = temp
        return delete_node.data

    def is_empty(self) -> bool:
        return len(self) == 0

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            if curr == self.head:
                break
        self.head = prev


if __name__ == "__main__":

    linked_list = CircularLinkedList()
    linked_list.insert_head(input("Inserting 1st at head ").split())
    linked_list.insert_head(input("Inserting 2nd at head ").split())
    print("\nPrint list: ")
    linked_list.print_list()

    linked_list.insert_tail(input("Inserting 1st tail ").strip())
    linked_list.insert_tail(input("Inserting 2nd at tail ").strip())
    print("\nPrint list: ")
    linked_list.print_list()

    linked_list.insert_nth(3, input("Inserting nth at position ").split())
    print("\nPrint list: ")
    linked_list.print_list()

    print("\nDelete head ")
    linked_list.delete_head()

    print('\nDelete tail ')
    linked_list.delete_tail()
    print('\nPrint linked list ')
    linked_list.print_list()

    print('\nReverse linked list ')
    linked_list.reverse()
    linked_list.print_list()

    print('\nString representation of linked list: ')
    print(linked_list)

    print(f"Length of linked list is: {len(linked_list)}")
