n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
# 접근법
# - 1초마다 동시에 a와 b를 움직인다 -> 쉽지않음
# - 그래서 개별적으로 시뮬레이션 진행 -> a와 b가 매초마다 어느 위치에 있었는지 기록한다. (index:흐른시간 / value:현재위치)

# a와 b가 매초마다 어느 위치에 있었는지 기록을 저장한 리스트
# ex. a[0] : 0초뒤 0에 위치 / a[1] : 1초뒤 -1에 위치
a = [0]
b = [0]

# a 시뮬레이션
curr_time = 0
curr_pos = 0
for k in range(n): #n개의 명령
    for _ in range(t[k]): # t[k]초동안 이동
        curr_time += 1 #1초가 추가로 흘렀다
        
        if d[k]=="L": #왼쪽으로 이동한다
            curr_pos -=1 #현재위치-1
        else:
            curr_pos +=1 
        
        a.append(curr_pos) # 흐른시간과 현재위치 저장

# b 시뮬레이션
curr_time = 0
curr_pos = 0
for k in range(m): #n개의 명령
    for _ in range(t2[k]): # t[k]초동안 이동
        curr_time += 1 #1초가 추가로 흘렀다
        
        if d2[k]=="L": #왼쪽으로 이동한다
            curr_pos -=1 #현재위치-1
        else:
            curr_pos +=1 
        
        b.append(curr_pos) # 흐른시간과 현재위치 저장

#더 짧은 시간동안 이동했던 리스트를 기준으로 만나는지 확인 : 각 리스트의 value가 같은지 확인
#만난다면 최초로 만나게 되는 시간 출력 (=인덱스 출력)
#아니라면 -1 출력
def meet(a, b):
    for t in range(min(len(a), len(b))):
        if a[t]==b[t]:
            return t
    return -1

print(meet(a,b))