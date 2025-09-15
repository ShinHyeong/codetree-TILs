n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

x, y = 0, 0 #시작위치
dir_num = 0
#순서대로 동 남 서 북
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for k in range(n):
    if dir[k]=="E":
        dir_num = 0
    if dir[k]=="S":
        dir_num = 1
    if dir[k]=="W":
        dir_num = 2
    if dir[k]=="N":
        dir_num = 3
    
    x += dx[dir_num] * dist[k]
    y += dy[dir_num] * dist[k]

print(x,y)