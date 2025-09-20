n, m = map(int, input().split())

# Please write your code here.
#nxm크기의 직사각형 2차원 배열 만들기
grid = [[0 for _ in range(m)] for _ in range(n)]

#남동북서 : x,y 변화량
dxs,dys = [1,0,-1,0],[0,1,0,-1]

#해당 x,y가 격자범위내에 존재하는가?
def in_range(x,y):
    return (0<=x and x<n) and (0<=y and y<m)

x,y = 0,0 #(x,y) #채우기 시작하는 칸
grid[x][y]=1 #1부터 채운다
dir_num = 0 #남쪽 방향으로 이동한다

# [2~n*m]도 채운다
#1. 숫자를 채울수 있다 : 만약 그 다음칸이 격자범위내에 있고 이미 채워진 칸이 아니라면
# - 다음칸으로 이동한다
# - 숫자를 채운다
#2. 숫자를 채울 수 없다 : not(채울수있는조건)
# - 방향을 바꾼다 (남->동->북->서)
# - 다음칸으로 이동한다
# - 숫자를 채운다

for i in range(2,n*m+1): 
    nx,ny = x+dxs[dir_num],y+dys[dir_num] #이동이 예상되는 다음칸
    if not(in_range(nx,ny) and grid[nx][ny]==0): 
        dir_num = (dir_num+1)%4 #방향을 바꾼다
    x,y = x+dxs[dir_num],y+dys[dir_num] #이동해야하는 다음칸으로 이동한다
    grid[x][y] = i #숫자 채우기

#수들끼리는 공백을 사이에 두고 완성된 nxm크기의 사각형출력
for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(grid[i][j], end=' ')
    print()