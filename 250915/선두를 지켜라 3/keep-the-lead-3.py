N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.

# n번에 걸쳐 a 시뮬레이션 : 흐른시간별 위치 기록
a = [0]
curr_pos=0
for k in range(N):
    for _ in range(t[k]): #t[k]동안 시뮬레이션
        curr_pos += v[k] #v[k]만큼 이동
        a.append(curr_pos) #이동거리 기록

# m번에 걸쳐 b 시뮬레이션  : 흐른시간별 위치 기록
b = [0]
curr_pos=0
for k in range(M):
    for _ in range(t2[k]): #t2[k]동안 시뮬레이션
        curr_pos += v2[k] #v2[k]만큼 이동
        b.append(curr_pos) #이동거리 기록

#명예의 전당에 올라가는 기준 : 매시간 마다 현재 선두인 사람
def fastest(curr):
    if a[curr]>b[curr]: #a가 선두일 경우
        return "A"
    if b[curr]>a[curr]: #b가 선두일 경우
        return "B"
    if a[curr]==b[curr]: #동시에 선두일 경우
        return "A&B"

cnt=0 #명예의 전당이 변경된 횟수
for curr in range(1,len(a)): #1시간 이후부터 명예의 전당 기록 시작
    if fastest(curr)!=fastest(curr-1) : #명예의 전당이 바뀌었습니다.
        cnt+=1

print(cnt)
