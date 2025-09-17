n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
#
#동남서북
dxs,dys = [1,0,-1,0],[0,-1,0,1]

#상하좌우 격자가 범위내에 있는지
def in_range(x,y):
    return (0<=x and x<n) and (0<=y and y<n)

# 상하좌우로 인접한 칸 중 숫자 1이 적혀있는 칸의 개수
def get_cnt(x,y):
    cnt=0
    for dx,dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy #상하좌우 인집한 격자 방문
        if in_range(nx,ny) and grid[nx][ny]==1:
            cnt+=1
    return cnt

# 상하좌우로 인접한 칸 중 숫자 1이 적혀있는 칸의 개수 >=3
ans=0
for i in range(n):
    for j in range(n):
        if get_cnt(i,j)>=3:
            ans += 1
print(ans)