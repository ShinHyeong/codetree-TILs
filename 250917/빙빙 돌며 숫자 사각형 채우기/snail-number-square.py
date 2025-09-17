n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
# n*m크기의 직사각형
grid = [[0 for _ in range(m)] for _ in range(n)]

# 동 : (0,+1)
# 남 : (+1,0)
# 서 : (0,-1)
# 북 : (-1,0)
dxs, dys = [0,1,0,-1], [1,0,-1,0]

# 3x2 크기
# (0,0) (0,1)
# (1,0) (1,1)
# (2,0) (2,1)
#채울 수 없는 경우 1 : 채워야할 칸이 격자 밖을 벗어난 경우
def in_range(x,y):
    return (0<=x and x<n) and (0<=y and y<m)

x,y = 0,0 #처음 인덱스
grid[x][y] = 1 #처음 값 : 1
dir_num = 0 #처음에 바라보는 방향 : 동쪽

for i in range(2, n*m+1): #2 ~ n*m 값 채우기
    nx,ny = x+dxs[dir_num], y+dys[dir_num]#그 다음값이
    if not (in_range(nx, ny) and grid[nx][ny]==0): #만약 채울 수 없다면
        dir_num = (dir_num + 1) % 4 #방향전환
    
    #방향에 맞게 전진
    x += dxs[dir_num] 
    y += dys[dir_num]

    #채우기
    grid[x][y] = i

#결과 출력
for i in range(n):
    for j in range(m):
        print(grid[i][j],end=' ')
    print()