n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
#현재 내가 위치한 r행 c열 -> 2차원 배열로 바꾸기 (x,y)
x,y = r-1,c-1

#상하좌우(udrl) 문자열과 매칭되는 숫자
mapper = {
    'R':0, #동
    'D':1, #남
    'U':2, #북
    'L':3 #서
}

dir_num = mapper[d] #현재 바라보는 방향

# 서로 반대방향끼리 번호(idx)더하면 3이 나오게 동남북서 설계
dxs,dys = [0,-1,1,0],[1,0,0,-1]

# 전진할 칸이 범위 밖인지 확인
def in_range(x,y):
    return (0<=x and x<n) and (0<=y and y<n)


#T번(=T초) 움직임
for _ in range(t):     
    # 전진할 칸
    nx, ny = x+dxs[dir_num], y+dys[dir_num]
    
    # 전진할 칸이 범위 밖인지 확인 : 전진할 칸이 범위 밖이면 방향이 뒤집힘
    # 이 때 방향을 바꾸는 데 1초의 시간이 소요됨
    if not in_range(nx, ny) : #범위 밖이다 -> 방향만 뒤집히고 전진하진 않음
        dir_num = 3 - dir_num
    else : #범위 내이다 -> 방향 그대로, 전진
        x,y = nx, ny
    
    

#2차원 배열 (x,y) -> 현재 내가 위치한 r행 c열로 바꾸기 
print(x+1,y+1)