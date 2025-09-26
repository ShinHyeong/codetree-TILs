N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.

def in_range(x,y):
    """
    주어진 좌표가 해당 범위밖인지 확인한다
    Returns:
        bool: 주어진 좌표가 범위 안이면 True
    """
    return (0<=x and x<N) and (0<=y and y<M)

def is_lee(start_x,start_y,dx,dy):
    """
    범위내에 있고 연속된 3개의 문자가 lee일 경우 True 리턴
    """
    x1,y1 = i,j
    x2,y2 = i+dx,j+dy
    x3,y3 = i+2*dx,j+2*dy
    return in_range(x1,y2) and in_range(x2,y2) and in_range(x3,y3) and arr[x1][y1]=='L' and arr[x2][y2]=='E' and arr[x3][y3]=='E'


#=====메인 실행 부분=====
    
#8개의 방향: 시계방향으로 동쪽부터 시작
DIRECTIONS=[
    (0,1), #동
    (1,1), #남동
    (1,0), #남
    (1,-1), #남서
    (0,-1), #서
    (-1,-1), #북서
    (-1,0), #북
    (-1,1) #북동
]

cnt = 0 #Lee의 갯수

#모든 문자열을 확인한다
for i in range(N):
    for j in range(M):
        #8개의 방향별로 lee를 찾는다
        for dx,dy in DIRECTIONS:
            if is_lee(i,j,dx,dy):
                cnt+=1

print(cnt)