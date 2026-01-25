N = int(input())
seats = input()

# Please write your code here.
### 요구사항 분석
# 원래 자리는 그대로
# 가장 가까운 두 사람 간의 거리를 최대로 하고싶다.


### 로직 설정
# 최적의 위치 찾기
    # 가장 먼 두 사람 간의 거리를 구한다
    # '1'간의 거리가 가장 먼 거리를 구한다 (=max_dist1)
    # 예외의 경우도 고려한다 (=max_dist2)
        # c1 : 0으로 시작, 1로 끝
        # c2 : 1로 시작, 0으로 끝
        # c3 : 0으로 시작, 0으로 끝
# max_dist2와 max_dist1 중 더 큰 값을 선택하여 최적의 위치에 1을 둔다
# 최단거리를 구한다

seats = list(seats)

max_dist1 = 0
max_i,max_j = -1,-1
for i in range(N):
    if seats[i]=='1':
        for j in range(i+1,N):
            if seats[j]=='1':
                if j-i > max_dist1:
                    max_dist = j-i
                    max_i,max_j = i, j

                break

max_dist2 = 0
max_idx = -1

if seats[0]=='0':
    dist = 0
    
    for i in range(N):
        if seats[i]=='1':
            break
        dist += 1

    if dist > max_dist2:
        max_dist2 = dist
        max_idx = 0

if seats[N-1]=='0':
    dist = 0
    
    for i in range(N-1,-1,-1):
        if seats[i]=='1':
            break
        dist += 1

    if dist > max_dist2:
        max_dist2 = dist
        max_idx = N-1

if max_dist2 >= max_dist//2:
    seats[max_idx] = '1'
else:
    seats[(max_i+max_j)//2] = '1'

ans = 1000
for i in range(N):
    if seats[i]=='1':
        for j in range(i+1,N):
            if seats[j]=='1':
                ans = min(j-i, ans)
                break
print(ans)