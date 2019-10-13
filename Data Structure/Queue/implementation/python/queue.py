class Queue:
    def __init__(self, max_size = 0):
        self.size = max_size
        self.arr = []
    
    def enqueue(self, data):
        if not self.isFull():
            self.arr.append(data)

    def dequeue(self):
        if not self.isEmpty():
            self.arr.pop(0)

    def isEmpty(self):
        return len(self.arr) == 0
    
    def isFull(self):
        return len(self.arr) == self.size

    def front(self):
        if not self.isEmpty():
            return self.arr[0]

    def rear(self):
        if not self.isEmpty():
            return self.arr[-1]
    
    def Qusize(self):
        return len(self.arr)

q = Queue(5)

n = int(input())

for i in range(n):
    k = int(input())
    q.enqueue(k)

print("Size of Queue = ", q.Qusize())
print("Queue is Full = ", q.isFull())
print("Queue is empty = ", q.isEmpty())
print("First element of queue = ", q.front())
print("Last element of queue = ", q.rear())
q.dequeue();
print("New First element of queue = ", q.front())

print("Queue element are :",end=' ')

while not q.isEmpty():
    print(q.front(),end=' ')
    q.dequeue()
print()
print("Queue is empty = ", q.isEmpty())