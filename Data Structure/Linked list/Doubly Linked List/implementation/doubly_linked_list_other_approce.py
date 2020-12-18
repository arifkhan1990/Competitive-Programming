from typing import Any


class Node:
    def __init__(self, data: int, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        return f"{self.data}"

    def get_data(self) -> int:
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.prev


class LinkedListIterator:
    def __init__(self, head):
        self.curr = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.curr:
            raise StopIteration
        else:
            value = self.curr.get_data()
            self.curr = self.curr.get_next()
            return value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        curr = self.head
        nodes = []
        while curr is not None:
            nodes.append(curr.get_data())
            curr = curr.get_next()
        return " ".join(str(item) for item in nodes)

    def __contains__(self, data: int):
        curr = self.head
        while curr:
            if curr.get_data() == data:
                return True
            curr = curr.get_next()
        return False

    def __iter__(self):
        return LinkedListIterator(self.head)

    def get_head_data(self):
        if self.head:
            return self.head.get_data()
        return None

    def get_tail_data(self):
        if self.tail:
            return self.tail.get_data()
        return None

    def set_head(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insert_before_node(self.head, node)

    def set_tail(self, node: Node) -> None:
        if self.head is None:
            self.set_head(node)
        else:
            self.insert_after_node(self.tail, node)

    def insert(self, data: int) -> None:
        node = Node(data)
        if self.head is None:
            self.set_head(node)
        else:
            self.set_tail(node)

    def insert_before_node(self, node: Node, node_to_insert: Node) -> None:
        node_to_insert.next = node
        node_to_insert.prev = node.prev

        if node.get_previous() is None:
            self.head = node_to_insert
        else:
            node.prev.next = node_to_insert
        node.prev = node_to_insert

    def insert_after_node(self, node: Node, node_to_insert: Node) -> None:
        node_to_insert.prev = node
        node_to_insert.next = node.next

        if node.get_next() is None:
            self.tail = node_to_insert
        else:
            node.next.prev = node_to_insert
        node.next = node_to_insert

    def insert_at_position(self, position: int, data: int) -> None:
        curr_position = 1
        new_node = Node(data)
        node = self.head
        while node:
            if curr_position == position:
                self.insert_before_node(node, new_node)
                return None
            curr_position += 1
            node = node.next
        self.insert_after_node(self.tail, new_node)

    def get_node(self, data: int) -> Node:
        node = self.head
        while node:
            if node.get_data() == data:
                return node
            node = node.get_next()
        raise Exception("Node not found")

    def delete_data(self, data):
        node = self.head
        if node is not None:
            if node == self.head:
                self.head = self.head.get_next()
            if node == self.tail:
                self.tail = self.tail.get_previous()
            self.remove_node_position(node)

    @staticmethod
    def remove_node_position(node: Node) -> None:
        if node.get_next():
            node.next.prev = node.prev

        if node.get_previous():
            node.prev.next = node.next

        node.next = None
        node.prev = None

    def is_empty(self):
        return self.head is None


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.get_head_data() is None
    linked_list.get_tail_data() is None
    linked_list.insert(10)
    linked_list.get_head_data()
    linked_list.get_tail_data()
    linked_list.insert_at_position(position=3, data=20)
    linked_list.get_head_data()
    linked_list.get_tail_data()
    linked_list.set_head(Node(1000))
    linked_list.get_head_data()
    linked_list.get_tail_data()
    linked_list.set_tail(Node(2000))
    for value in linked_list:
        print(value)
