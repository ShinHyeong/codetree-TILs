dirs = input()

# Please write your code here.
x, y = 0, 0 #현재위치 (0,0)
dir_num=3 #처음엔 북쪽을 향한 상태

#동 남 서 북
dx, dy = [1,0,-1,0],[0,-1,0,1]


N = len(dirs) #N개의 명령
for i in range(N):
    if dirs[i] == "L": #반시계방향으로 90도 회전
        dir_num = (dir_num -1 +4) % 4
    elif dirs[i] == "R": #시계방향으로 90도 회전
        dir_num = (dir_num + 1) % 4
    elif dirs[i] == "F": #바라보고 있는 방향으로 한 칸 이동
        x += dx[dir_num]
        y += dy[dir_num]
    
print(x,y)