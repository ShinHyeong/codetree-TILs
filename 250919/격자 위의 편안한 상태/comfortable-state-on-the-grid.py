n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
# 0이 채워진 n*n 크기의 격자
grid = [[0 for _ in range(n*n)] for _ in range(n*n)]

# (0,0) (0,1)
# (1,0) (1,1)
# 동남서북
dxs,dys = [0,1,0,-1],[1,0,-1,0]


#해당 칸이 격자를 벗어낫는가?
def in_range(x,y):
    return (0<=x and x<n) and (0<=y and y<n)

#편안한 상태에 있는가?
#편안한 상태란 : 방금 칠해진 칸을 기점으로 
#위아래 양옆으로 인접한 4개의 칸 중 격자를 벗어나지 않는 칸에 
#색칠되어 있는칸이 정확히 3개인 경우
def is_comfortable(x,y):
    cnt=0
    for dir_num in range(4):
        nx,ny = x+dxs[dir_num], y+dys[dir_num] #위아래 양옆으로 인접한 4개의 칸 중
        if in_range(nx,ny) and grid[nx][ny]==1:#격자를 벗어나지 않고, 색칠되어있는가? 
            cnt+=1
    return cnt==3  #그 칸이 정확히 3개인가?

for p in points: #m번에 걸쳐
    x,y = p[0]-1, p[1]-1 #색칠할 칸 위치 (r,c)를 2차원 배열로 옮긴다
    grid[x][y] = 1 #색칠한다 (1)
    print(1 if is_comfortable(x,y) else 0) #편안한 상태에 놓여있는가?
                                        #해당 칸이 편안한 상태라면 1, 아니라면 0 출력