class Node:
    def __init__(self, value = None, pointer = None):
        self.value = value
        self.pointer = pointer

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return not bool(self.head)
    
    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.pointer
            return value
    
    def enqueue(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            if self.tail:
                self.tail.pointer = node
            self.tail = node
    
    def size(self):
        node = self.head
        num_nodes = 0
        while node:
            num_nodes += 1
            node = node.pointer
        return num_nodes
    
    def peek(self):
        return self.head.value
    
    def _print(self):
        node = self.head
        while node:
            print(node.value,end=' ')
            node = node.pointer
        print()



if __name__ == '__main__':
    queue = LinkedQueue()
    print("Is the queue empty? ", queue.isEmpty())
    print("Adding 1 to 10 in queue element ")
    for i in range(1,11):
        queue.enqueue(i)
    print("Queue size : ", queue.size())
    print("Queue front data : ", queue.peek())
    print("Remove queue front element :", queue.dequeue())
    print("Queue new front data : ", queue.peek())
    print("Is the queue empty? ", queue.isEmpty())
    print("Printing the queue element :",end=' ')
    queue._print()
    queue.enqueue(44)
    queue.enqueue(99)
    print("Printing the new queue element :",end=' ')
    queue._print()
    print("Queue size : ", queue.size())
    print("Queue front data : ", queue.peek())