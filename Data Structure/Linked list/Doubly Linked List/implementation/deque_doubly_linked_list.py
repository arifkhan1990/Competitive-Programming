class DeublyLinkedList:

    class Node:
        __slots__ = "prev", "data", "next"

        def __init__(self, link_p, element, link_n):
            self.prev = link_p
            self.next = link_n
            self.data = element

        def has_next_and_prev(self):
            return " Prev -> {}".format(self.prev is not None, self.next is not None)

        def __init__(self):
            self.header = self.Node(None, None, None)
            self.trailer = self.Node(None, None, None)
            self.header.next = self.trailer
            self.trailer.prev = self.header
            self.size = 0

        def __len__(self):
            return self.size

        def is_empty(self):
            return self.__len__() == 0

        def insert(self, predecessor, e, successor):
            new_node = self.Node(predecessor, e, successor)
            predecessor.next = new_node
            successor.prev = new_node
            self.size += 1
            return self

        def delete(self, node):
            predecessor = node.prev
            successor = node.next

            predecessor.next = successor
            successor.prev = predecessor
            self.size -= 1
            temp = node.data
            node.prev = node.next = node.data = None
            del node
            return temp

        class LinkedDeque(DeublyLinkedList):
            def first(self):
                if self.is_empty():
                    raise Exception("List is empty!")
                return self.header.next.data

            def last(self):
                if self.is_empty():
                    raise Exception("List is empty!")
                return self.trailer.prev.data

            def add_first(self, data):
                return self.insert(self.header, data, self.header.next)

            def add_last(self, data):
                return self.insert(self.trailer.prev, data, self.trailer)

            def remove_first(self):
                if self.is_empty():
                    raise IndexError("Lise is empty!")
                return self.delete(self.header.next)

            def remove_last(self):
                if self.is_empty():
                    raise IndexError("List is empty!")
                return self.delete(self.trailer.prev)
