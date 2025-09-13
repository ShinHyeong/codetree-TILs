n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
a = [0] # 흐른 시간(시간단위)별 a가 이동한 거리
b = [0] # 흐른 시간(시간단위)별 b가 이동한 거리

#a 시뮬레이션 : 흐른 시간별 a가 이동한 거리 기록
curr_dist = 0 #흐른 시간 초기화
for k in range(n):
    for _ in range(t[k]): #t[k]동안
        curr_dist += v[k] #1시간이 흘렀다
        a.append(curr_dist) #curr_dist만큼 움직였다는 것을 기록

#b 시뮬레이션 : 흐른 시간별 b가 이동한 거리 기록
curr_dist = 0 #흐른 시간 초기화
for k in range(m):
    for _ in range(t2[k]): #t2[k]동안
        curr_dist += v2[k] #1시간이 흘렀다
        b.append(curr_dist) #curr_dist만큼 움직였다는 것을 기록

cnt = 0 #선두가 바뀌는 횟수
#1시간 단위로 보면서 선두가 바뀌면 cnt+=1
for i in range(2, min(len(a),len(b))):
    #선두가 바뀌는지 어떻게 아는가? : 현재선두 != 이전선두 
    #1) a[i]>b[i] and a[i-1]<=b[i-1]
    #2) b[i]<a[i] and a[i-1]>=b[i-1]
    if (a[i]>b[i] and a[i-1]<=b[i-1]) or (b[i]>a[i] and a[i-1]>=b[i-1]):
        cnt+=1

print(cnt)