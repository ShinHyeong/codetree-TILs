N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
def in_range(x,y): #(x,y)가 격자범위내에 있는가
    return (0<=x and x<N) and (0<=y and y<N)

#동남서북 : x,y변화량
dxs,dys = [0,1,0,-1],[1,0,-1,0]

commands = list(str) #명령어 모음

#시작 조건
x,y = N//2,N//2#가운데 위치에서 시작
dir_num = 3 #북쪽을 향한채로 시작
sum_val = board[x][y] #시작위치를 포함하여 위치를 이동할 떄마다 더해진 총합

for c in commands: #명령어 하나씩 처리
    if c=="L": #반시계방향 90도 전환
        dir_num = (dir_num-1+4)%4    
    if c=="R": #시계방향 90도 전환
        dir_num = (dir_num+1)%4
    if c=="F": #주어진 방향으로 한칸 전진
        nx,ny = x+dxs[dir_num],y+dys[dir_num] #이동이 예상되는 다음칸
        if in_range(nx,ny): #격자범위내에 있는가
            x,y=nx,ny #이동한다
            sum_val+=board[x][y] #더한다

print(sum_val)