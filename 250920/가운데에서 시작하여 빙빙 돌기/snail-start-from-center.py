n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
x,y = n//2, n//2 #nxn 크기의 정사각형 가운데에서 시작
grid[x][y]=1 #1부터 시작
dir_num =0 #이동하는 방향 초기화

#동->북->서->남 : x,y변화량
dxs,dys = [0,-1,0,1],[1,0,-1,0]

#주어진 x,y가 격자 범위내에 있는가
def in_range(x,y):
    return (0<=x and x<n) and (0<=y and y<n)

for i in range(2, n*n+1): #2~n*n 를 채워넣는다
    nx,ny = x+dxs[dir_num],y+dys[dir_num] #이동이 예상되는 다음칸
    if not(in_range(nx,ny) and grid[nx][ny]==0): #다음칸으로 이동못한다
        dir_num = (dir_num+1)%4 #동->북->서->남 방향으로 회전

    x,y = x+dxs[dir_num],y+dys[dir_num] #다음칸으로 이동한다

    grid[x][y]=i #숫자를 채워넣는다

#완성된 사각형 출력
for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(grid[i][j], end=' ')
    print()