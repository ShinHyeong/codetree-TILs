n, m = map(int, input().split())

# Please write your code here.
# 0으로 채워진 nxm크기의 격자
grid = [[0 for _ in range(m)] for _ in range(n)]

#동남서북 : x,y의 변화량
dxs,dys = [0,1,0,-1],[1,0,-1,0]

#x,y가 범위내에 있는가
def in_range(x,y):
    return (0<=x and x<n) and (0<=y and y<m)

x,y = 0,0 #시작하는 칸
grid[x][y] = chr(65) #A부터 채운다
dir_num = 0#다음칸으로 이동하는 방향

# 총 n*m칸 채우기
# 65 66 67 ... 65+(n*m-1)

# 91 92 93
# 65 66 67
for i in range(66, 65+n*m): #B~Z까지 채우는데 Z이후엔 다시 A부터 채운다
    
    nx,ny = x+dxs[dir_num],y+dys[dir_num]#이동이 예상되는 다음칸
    if not(in_range(nx,ny) and grid[nx][ny]==0): #숫자를 채울 수 없다 : not(숫자를 채울 수 있는 조건)
        dir_num = (dir_num+1)%4 #회전한다 : 동->남->서->북
    
    x,y = x+dxs[dir_num],y+dys[dir_num]#다음칸으로 이동한다
    
    if i > 90: #Z이후엔 다시 A부터 채운다 #A의 아스키 코드 : 65 #Z의 아스키 코드 : 90
        i = 65 + (i - 91)
    grid[x][y] = chr(i) #알파벳을 채운다

for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(grid[i][j], end =' ')
    print()