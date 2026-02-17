n, m = map(int, input().split())
s = input()

stack_l = list(s)
stack_r = []

for _ in range(m):
    cmd = input().split()
    if cmd[0] == "L":
        stack_r.append(stack_l.pop())
    if cmd[0] == "R":
        stack_l.append(stack_r.pop())
    if cmd[0] == "D":
        stack_r.pop()
    if cmd[0] == "P":
        stack_l.append(cmd[1])

print("".join(stack_l)+"".join(reversed(stack_r)))
