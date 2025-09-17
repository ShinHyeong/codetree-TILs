N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

# 좌표평면 -> 이차원배열
#       (0, 1)
# (-1,0)(0,0)(+1,0)
#       (0,-1)
dxs,dys = [+1,0,-1,0],[0,-1,0,+1]

# 방향 문자열 -> 번호로 매핑
mapper = {
    "E":0, #동
    "S":1, #남
    "W":2, #서
    "N":3 #북
}

# 상하좌우로 x/y:최대/최소 100*10
grid = [[0] * (1+100*10*2) for _ in range(1+100*10*2)]

#시작좌표 (0,0)
x,y = (1+100*10*2)//2, (1+100*10*2)//2 


#시작점인지 확인하는 함수
def is_startLine(x,y):
    return x==(1+100*10*2)//2 and y==(1+100*10*2)//2

#N번 이동 (1초에 1칸 이동)
#만약 시작점을 만났다면 종료하고
#걸린 시간을 리턴하는 함수. (단, 다시 시작점으로 못 돌아왔으면 -1)
def moving(x,y):
    elapsed_time = 0
    for k in range(N): #k번째 명령
        dir_num = mapper[dir[k]] #방향에 맞추어
        for i in range(dist[k]): #dist[k]칸 이동 = dist[k]초 동안 이동
            x += dxs[dir_num] #한칸 전진
            y += dys[dir_num]
            elapsed_time +=1 #1초가 흘렀다
            #만약 한칸 전진했을 때 시작점이라면 종료
            if is_startLine(x,y):
                return elapsed_time
    return -1

print(moving(x,y))