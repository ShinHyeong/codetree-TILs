commands = input()

# Please write your code here.

# 좌표평면 -> 2차원배열
# 동남서북
dxs,dys = [1,0,-1,0], [0,-1,0,1]

#시작 조건
x,y = 0,0 #좌표평면 (0,0)
dir_num = 3 #시작방향: 북쪽

#현재 시작점인지 판단하는 함수
def is_startLine(x,y):
    return x==0 and y==0

def moving(x, y):
    global dir_num
    elapsed_time=0
    #N개의 명령 하나씩 처리
    for c in commands: 
        if c=="L": #왼쪽 90도 방향전환(반시계방향)
            dir_num = (dir_num -1 +4) %4
        elif c=="R": #오른쪽 90도 방향전환(시계방향)
            dir_num = (dir_num +1) %4
        else: #c=="F" : 1칸 전진
            x += dxs[dir_num]
            y += dys[dir_num]

        elapsed_time +=1 #1초 흘렀습니다
        if is_startLine(x, y):#만약 시작점이라면 종료
            return elapsed_time #걸리는 시간 출력
    
    #만약 n번 이동을 진행했는데도 시작점으로 되돌아오지 못했다면 -1
    return -1 

#다시 시작점으로 되돌아오는데 걸리는 시간 출력. 
print(moving(x,y))