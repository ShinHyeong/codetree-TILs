n = int(input())
cmd = []
num = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
from collections import deque
dq = deque()

for i in range(n):
    if cmd[i]=="push_front":
        dq.appendleft(num[i])
    if cmd[i]=="push_back":
        dq.append(num[i])
    if cmd[i]=="pop_front":
        print(dq.popleft())
    if cmd[i]=="pop_back":
        print(dq.pop())
    if cmd[i]=="size":
        print(len(dq))
    if cmd[i]=="empty":
        print(1 if not dq else 0)
    if cmd[i]=="front":
        print(dq[0])
    if cmd[i]=="back":
        print(dq[-1])
    
    
    