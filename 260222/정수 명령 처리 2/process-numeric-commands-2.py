N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.
from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    def push(self, item):
        self.dq.append(item)
    def empty(self):
        return not self.dq
    def size(self):
        return len(self.dq)
    def pop(self):
        if self.empty():
            raise Exception("Queue is Empty")
        return self.dq.popleft()
    def front(self):
        if self.empty():
            raise Exception("Queue is Empty")
        return self.dq[0]

dq = Queue()
for i in range(N):
    if command[i] == "push":
        dq.push(A[i])
    if command[i] == "pop":
        print(dq.pop())
    if command[i] == "size":
        print(dq.size())
    if command[i] == "empty":
        print(int(dq.empty()))
    if command[i] == "front":
        print(dq.front())