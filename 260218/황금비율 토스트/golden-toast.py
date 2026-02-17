n, m = map(int, input().split())
s = input()
s = list(s)
arrow = len(s)
#print(arrow, s)

for _ in range(m):
    cmd = input().split()
    if cmd[0] == "L":
        if arrow > 0:
            arrow -= 1
    if cmd[0] == "R":
        if arrow < len(s):
            arrow += 1
    if cmd[0] == "D":
        if arrow < len(s):
            s = s[:arrow]+s[arrow+1:]
    if cmd[0] == "P":
        to_add = cmd[1]
        s = s[:arrow]+[to_add]+s[arrow:]
        arrow += 1
    #print(arrow, s)
print("".join(s))