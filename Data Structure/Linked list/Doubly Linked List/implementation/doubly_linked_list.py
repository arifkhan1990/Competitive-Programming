from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return f"{self.data}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __str__(self):
        return "->".join(str(item) for item in iter(self))

    def __len__(self):
        return len(tuple(iter(self)))

    def insert_head(self, data: Any) -> None:
        self.insert_nth(0, data)

    def insert_tail(self, data: Any) -> None:
        self.insert_nth(len(self), data)

    def insert_nth(self, idx: int, data: Any) -> None:
        if not 0 <= idx <= len(self):
            raise IndexError("List out of range.")
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        elif idx == 0:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        elif idx == len(self):
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        else:
            temp = self.head
            for _ in range(idx - 1):
                temp = temp.next
            temp.next.previous = new_node
            new_node.next = temp.next
            temp.next = new_node
            new_node.previous = temp

    def delete_head(self):
        return print(self.delete_nth(0))

    def delete_tail(self):
        return print(self.delete_nth(len(self) - 1))

    def delete_nth(self, idx: int = 0):
        if not 0 <= idx <= len(self) - 1:
            raise IndexError('List index out of range.')
        delete_node = self.head
        if len(self) == 1:
            self.head = self.tail = None
        elif idx == 0:
            self.head = self.head.next
            self.head.previous = None
        elif idx == len(self) - 1:
            delete_node = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            temp = self.head
            for _ in range(idx):
                temp = temp.next
            delete_node = temp
            temp.next.previous = temp.previous
            temp.previous.next = temp.next
        return delete_node.data

    # delete target value
    def delete(self, data: Any):
        curr = self.head

        while curr.data != data:
            if curr.next:
                curr = curr.next
            else:
                return "No data matching given value!"

            if curr == self.head:
                self.delete_head()
            elif curr == self.tail:
                self.delete_tail()
            else:
                curr.previous.next = curr.next
                curr.next.previous = curr.previous
        return data

    def is_empty(self) -> bool:
        return len(self) == 0

    def print_list(self):
        print(self)

    def reverse(self):
        curr = self.head
        prev = None

        while curr:
            prev = curr.previous
            curr.previous = curr.next
            curr.next = prev
            curr = curr.previous
        if prev is not None:
            self.head = prev.previous


if __name__ == "__main__":

    linked_list = DoublyLinkedList()
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
