N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

# Please write your code here.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def empty(self):
        return not self.items
    
    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def top(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items[-1]
    
st = Stack()
for i in range(N):
    if command[i]=="push":
        st.push(value[i])
    if command[i]=="pop":
        print(st.pop())
    if command[i]=="size":
        print(st.size())
    if command[i]=="empty":
        print(int(st.empty()))
    if command[i]=="top":
        print(st.top())