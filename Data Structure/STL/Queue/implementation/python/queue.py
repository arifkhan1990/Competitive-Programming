import queue

q = queue.Queue()

n = int(input())

for i in range(n):
    m = int(input())
    q.put(m)

print("Queue size : ", q.qsize())
print("Queue first element : ",q.get())
print("Check Queue is full or not : ", q.full())
print("Queue is empty or not : ", q.empty())

while not q.empty():
    print(q.get(),end=' ')
    q.pop()

print("Queue is empty or not : ", q.empty())