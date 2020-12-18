# Recursive Prorgam to create a Linked List from a sequence and
# print a string representation of it.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        """Returns a visual representation of the node and all its following nodes."""
        ans = ""
        temp = self
        while temp:
            ans += f"<{temp.data}> --> "
            temp = temp.next
        ans += "<END>"
        return ans


def make_linked_list(data_list):
    """Creates a Linked List from the elements of the given sequence
    (list/tuple) and returns the head of the Linked List."""
    if not data_list:
        raise Exception("The Data List is empty!")

    head = Node(data_list[0])
    curr = head
    for data in data_list[1:]:
        curr.next = Node(data)
        curr = curr.next
    return head


list_data = [1, 44, 22, 31, 54, 66, 77, 99]
print(f"List: {list_data}")
print("Creating Linked List from List.")
linked_list = make_linked_list(list_data)
print("Linked list: ")
print(linked_list)
