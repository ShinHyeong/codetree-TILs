R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.

#이동할 수 있는가? : 현재위치색과 다른색인지
def is_diff(x1,y1,x2,y2):
    return grid[x1][y1] != grid[x2][y2]

#조건1:현재위치 색과 다른 색만 이동 가능
#조건2:현재위치에서 최소 한칸이상 오른쪽, 최소 한칸이상 아래쪽에 있어야함
#조건3:시작,도착 지점 제외 중간에 점프한 지점 2곳만 -> 3번만 점프 가능하다

#(0,0)에서 (r-1,c-1)로 이동
x,y = 0,0 #처음시작지점
move_limit = 3 #점프가능횟수

# A (0,0) -> B -> C -> D (r-1,c-1) 지점이라고 할때
# 1. B지점을 찾는다
B_list = []
for i in range(x+1, R):
    for j in range(y+1, C):
        if is_diff(x,y,i,j):
            B_list.append((i,j))

# 2. B지점별로 C지점의 갯수를 센다
# - 단, C지점은 x<r-1 and y<c-1 여야한다.
cnt=0
for b in B_list:
    for i in range(b[0]+1, R):
        for j in range(b[1]+1, C):
            if is_diff(b[0],b[1],i,j) and (i<R-1 and j<C-1):
                cnt+=1
print(cnt if grid[x][y]!=grid[R-1][C-1] else 0) #만약 시작점과 끝점의 색이 같다면 0


