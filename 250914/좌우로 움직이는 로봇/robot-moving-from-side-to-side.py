n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
# n회동안 A 시뮬레이션 : 흐른시간(초)별 a의 위치
# m회동안 B 시뮬레이션
a = [0]
curr_time, curr_pos = 0, 0

for k in range(n):
    for i in range(t[k]):
        curr_time += 1 #1초가 흘렀다
        
        if d[k]=="L": #왼쪽이동
            curr_pos -=1
        else: #오른쪽이동
            curr_pos +=1

        a.append(curr_pos) #1초마다 어느위치에 있는지 추가

b = [0]
curr_time, curr_pos = 0, 0

for k in range(m):
    for i in range(t_b[k]):
        curr_time += 1 #1초가 흘렀다
        
        if d_b[k]=="L": #왼쪽이동
            curr_pos -=1
        else: #오른쪽이동
            curr_pos +=1

        b.append(curr_pos) #1초마다 어느위치에 있는지 추가

#더 작은 길이의 리스트를 더 큰 길이의 리스트 길이에 맞춤. : 추가된 인덱스는 마지막 인덱스값으로 채움
#ex. 더 큰 길이의 리스트 : 1 2 3 4 5 (len=5)
# 더 작은 길이의 리스트 : 1 2 (len=2)
# idx=2,3,4의 값을 채워야함
longest = a if len(a)>len(b) else b
shortest = a if len(a)<len(b) else b
for _ in range( len(longest) - len(shortest) ):
    shortest.append(shortest[len(shortest)-1])

#a,b가 같은시간 같은위치에 있으면 카운팅
#조건1 : 처음위치(idx=0)은 횟수에 포함시키지 않음. 즉, idx=1 부터 돌림
#조건2 : 바로 직전에 같은위치에 있으면 안됨
cnt=0
for curr in range(1, len(longest)): #조건1
    if a[curr]==b[curr] and a[curr-1]!=b[curr-1]: #조건2
        cnt +=1 

print(cnt)