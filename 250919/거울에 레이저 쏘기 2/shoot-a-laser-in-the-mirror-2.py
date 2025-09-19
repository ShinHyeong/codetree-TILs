n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
#처음 부딪히는 칸과 레이저 쏘는 방향
# if n=3, 격자밖 4*3개의 위치
#n=3 k=1 -> (0,0) 남 
#n=3 k=2 -> (0,1) 남 
#n=3 k=3 -> (0,2) 남 
#==> if k<=n, (0,_) : x는 0으로 고정 /y는 0부터 +1  

#n=3 k=4 -> (0,2) 서 
#n=3 k=5 -> (1,2) 서 
#n=3 k=6 -> (2,2) 서 
#==> elif k<=n*2, (_,n-1) : x는 0부터 +1/y는 n-1값으로 고정

#k=7 -> (2,2) 북
#k=8 -> (2,1) 북
#k=9 -> (2,0) 북 
#==> elif k<=n*3, (n-1,_) : x는 n-1로 고정/y는 n-1부터 -1됨

#k=10 -> (2,0) 동
#k=11 -> (1,0) 동
#k=12 -> (0,0) 동 
#==> elif k<=n*4, (_,0) : x는 n-1부터 -1됨/y는 0으로 고정

#(n,k)와 변하는값(차음시작하는 x or y)의 관계
#   (3,1)     (3,2)    (3,3) 
#y =1%3-1(=0) 2%3-1(=1)  3-1(=2)
#   (3,4)     (3,5)    (3,6) 
#y =4%3-1(=0) 5%3-1(=1)  3-1(=2)
#   (3,7)     (3,8)    (3,9) 
#y =7%3-1(=0) 8%3-1(=1)  n-1(=2)
#...
#일반화 : y= k%n-1 , 단, k가 n의 배수라면, y=n-1 


#(0,0)(0,1)
#(1,0)(1,1)
#동북남서 0 12 3
dxs,dys = [0,-1,1,0],[1,0,0,-1]

#레이저 쏘는 방향과 처음 부딪히는 칸
def pos_k(k):
    x,y, dir_num = 0,0, 0

    if k<=n: 
        dir_num = 2 #남
        x=0
        y=k%n-1 if k%n!=0 else n-1
    elif k<=n*2:
        dir_num = 3 #서
        x=k%n-1 if k%n!=0 else n-1
        y=n-1
    elif k<=n*3:
        dir_num = 1 #북
        x=n-1
        y=k%n-1 if k%n!=0 else n-1
    else: #k<=n*4
        dir_num = 0 #동
        x=k%n-1 if k%n!=0 else n-1
        y=0

    return (dir_num, (x,y))

# \ 북->동 /동->북 /남->서 /서->남 으로 바뀜 : (북,동)(남,서) (0,1)(2,3)
# / 북->서 /동->남 /남->동 /서->북 으로 바뀜 : (북,서)(동,남) (0,3)(1,2)
def rotate(dir_num, mirror):
    if mirror == "\\":
        if dir_num == 0 or dir_num==2:
            dir_num +=1
        elif dir_num ==1 or dir_num==3:
            dir_num -=1
        
    elif mirror == "/":
        dir_num = 3 - dir_num 
    
    return dir_num

#해당 칸이 격자범위내에 있는지 확인
def in_range(x,y):
    return (0<=x and x<n) and (0<=y and y<n)

cnt=0 # 거울에 튕기는 횟수
# 해당 위치에서 레이저를 쏜다
dir_num = pos_k(k)[0] #해당 방향으로 레이저를 쏜다
x,y = pos_k(k)[1] #처음 부딪히는 칸 (=시작위치)
while True:
    dir_num = rotate(dir_num, grid[x][y]) #회전하고 레이저방향 업데이트
    cnt+=1#카운팅
    #다음칸으로 가기 전 다음칸이 격자범위에 있는지 확인
    nx,ny = x+dxs[dir_num],y+dys[dir_num]
    if in_range(nx,ny):
        x,y = nx,ny #한칸 이동
    else:
        break #종료

# 거울에 튕기는 횟수 출력
print(cnt)