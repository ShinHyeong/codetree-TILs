n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.

#동->북->서->남 : x,y변화량
dxs,dys = [0,-1,0,1],[1,0,-1,0]

#완성된 사각형 출력
def print_rect():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end=' ')
        print()

### 로직 ###
#n=3
#현재칸에서
#-> 이동방향 변경 :동쪽 -> (1칸 이동 -> 숫자를 채워넣는다) x1
#-> 이동방향 변경 :북쪽 -> (1칸 이동 -> 숫자를 채워넣는다) x1
#-> 이동방향 변경 :서쪽 -> (1칸 이동 -> 숫자를 채워넣는다) x2
#-> 이동방향 변경 :남쪽 -> (1칸 이동 -> 숫자를 채워넣는다) x2
#-> 이동방향 변경 :동쪽 -> (1칸 이동 -> 숫자를 채워넣는다) x(n-1)

#n=5
#현재칸에서
#-> 이동방향 변경 :동쪽 -> (1칸 이동 -> 숫자를 채워넣는다) x1
#-> 이동방향 변경 :북쪽 -> (1칸 이동 -> 숫자를 채워넣는다) x1
#-> 이동방향 변경 :서쪽 -> (1칸 이동 -> 숫자를 채워넣는다) x2
#-> 이동방향 변경 :남쪽 -> (1칸 이동 -> 숫자를 채워넣는다) x2
#-> 이동방향 변경 :동쪽 -> (1칸 이동 -> 숫자를 채워넣는다) x3
#-> 이동방향 변경 :북쪽 -> (1칸 이동 -> 숫자를 채워넣는다) x3
#-> 이동방향 변경 :서쪽 -> (1칸 이동 -> 숫자를 채워넣는다) x4
#-> 이동방향 변경 :남쪽 -> (1칸 이동 -> 숫자를 채워넣는다) x4
#-> 이동방향 변경 :동쪽 -> (1칸 이동 -> 숫자를 채워넣는다) x(n-1)

x,y = n//2, n//2 #nxn 크기의 정사각형 가운데에서 시작
grid[x][y]=1 #1부터 채운다
dir_num =0 #이동하는 방향 초기화 : 동

i = 2
step = 1

while i <= n*n: #2~n*n 를 채워넣는다
    if step==n:
        step=n-1
    for _ in range(2):
        for _ in range(step):
            x,y = x+dxs[dir_num],y+dys[dir_num] #다음칸으로 이동한다
            grid[x][y]=i #숫자를 채워넣는다
            i+=1
            if i>n*n:
                break
        if i>n*n:
                break
        dir_num = (dir_num+1)%4 #동->북->서->남 으로 이동방향 변경
    step+=1


#완성된 사각형 출력
for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(grid[i][j], end=' ')
    print()