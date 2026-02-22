n, k = map(int, input().split())

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
for p in range(1,n+1):
    dq.push(p)

while dq.size() > 0: #n명의 사람이 모두 제거될 때까지 진행
    for i in range(k-1):
        dq.push(dq.pop())
    print(dq.pop(),end=" ") #k번째 사람 제거
