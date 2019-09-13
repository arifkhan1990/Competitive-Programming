class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

q = Queue()

q.enqueue(4)
q.enqueue('dogs')
q.enqueue(True)

print("Queue size: ", q.size())
print("Empty or not : ", q.isEmpty())
