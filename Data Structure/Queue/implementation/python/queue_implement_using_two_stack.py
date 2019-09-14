class Queue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def enqueue(self, data):
        while self.out_stack:
            self.in_stack.append(self.out_stack.pop())

        self.in_stack.append(data)

        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())


    def dequeue(self):
        if self.out_stack:
            self.out_stack.pop()
    
    def size(self):
        return len(self.out_stack)
    
    def frontData(self):
        if self.out_stack:
            return self.out_stack[-1]

    def __repr__(self):
        if self.out_stack:
            return '{}'.format(self.out_stack)
    
    def isEmpty(self):
        return not (bool(self.out_stack))



if __name__ == '__main__':
    queue = Queue()
    print("Is the queue empty? ", queue.isEmpty())
    print("Adding 1 to 10 in queue element ")
    for i in range(1,11):
        queue.enqueue(i)
    print("Queue size : ", queue.size())
    print("Queue front data : ", queue.frontData())
    print("Remove queue front element ")
    queue.dequeue()
    print("Queue new front data : ", queue.frontData())
    print("Is the queue empty? ", queue.isEmpty())
    print("Printing the queue element : ")
    print(queue)
    queue.enqueue(44)
    queue.enqueue(99)
    print("Printing the new queue element : ")
    print(queue)
    print("Queue size : ", queue.size())
    print("Queue front data : ", queue.frontData())