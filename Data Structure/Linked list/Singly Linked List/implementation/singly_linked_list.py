class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        return len(tuple(iter(self)))

    def __repr__(self):
        return "->".join([str(item) for item in self])

    def __getitem__(self, idx):
        # Indexing Support. Used to get a node at particular position
        if not 0 <= idx < len(self):
            raise ValueError("list index out of range.")
        for i, node in enumerate(self):
            if i == idx:
                return node

    def __setitem__(self, idx, data):
        # Used to change the data of a particular node
        if not 0 <= idx < len(self):
            raise ValueError("list index out of range.")
        current = self.head
        for _ in range(idx):
            current = current.next
        current.data = data

    def insert_head(self, data) -> None:
        self.insert_nth(0, data)

    def insert_tail(self, data) -> None:
        self.insert_nth(len(self), data)

    def insert_nth(self, idx: int, data) -> None:
        if not 0 <= idx <= len(self):
            raise ValueError("List index out of range.")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif idx == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(idx - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def print_list(self) -> None:
        print(self)

    def delete_head(self):
        return print(self.delete_nth(0))

    def delete_tail(self):
        return print(self.delete_nth(len(self) - 1))

    def delete_nth(self, idx: int = 0):
        if not 0 <= idx <= len(self) - 1:
            raise IndexError("list index out of range.")
        delete_node = self.head

        if idx == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(idx - 1):
                temp = temp.next
            delete_node = temp.next
            temp.next = temp.next.next
        return delete_node.data

    def is_empty(self) -> bool:
        return self.head is None

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


if __name__ == "__main__":

    linked_list = SinglyLinkedList()
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

    print('\nReading /changing Node data using indexing: ')
    print(f"Element at Position 1: {linked_list[1]}")
    linked_list[1] = input("Enter New Value: ").strip()
    print("New List: ")
    print(linked_list)

    print(f"Length of linked list is: {len(linked_list)}")
