N = int(input())
seats = input()

# Please write your code here.
### 요구사항 분석
# 원래 자리는 그대로
# 가장 가까운 두 사람 간의 거리를 최대로 하고싶다.


### 로직 설정
# c1 : 0으로 시작, 1로 끝 -> 맨 앞에 1을 붙인다
    #0010000001000001 
    #0000001000001
# c2 : 1로 시작, 0으로 끝 -> 맨 뒤에 1을 붙인다
# c3 : 0으로 시작, 0으로 끝 -> 맨 앞과 맨 뒤에 1을 붙인다
# 이렇게 처리했을 때 가까운거리를 구한다

# 다시 원상복구
# 가장 먼 두 사람 간의 거리를 구하고 가운데에 1을 넣는다
# 이렇게 처리했을 때 가까운 거리를 구한다

# 둘 중 큰 값을 리턴한다

seats = list(seats)

def get_min_dist(arr):
    min_dist = 1000

    for i in range(N):
        if seats[i]=='1':
            for j in range(i+1,N):
                if seats[j]=='1':
                    min_dist = min(j-i,min_dist)
                    break

    return min_dist

a1 = -1

if seats[0]=='0':
    seats[0]='1'
    a1 = get_min_dist(seats)
    seats[0]='0'

if seats[N-1]=='0':
    seats[N-1]='1'
    a1 = max(get_min_dist(seats), a1)
    seats[N-1]='0'

max_dist = 0
max_i,max_j = -1,-1
for i in range(N):
    if seats[i]=='1':
        for j in range(i+1,N):
            if seats[j]=='1':
                if j-i > max_dist:
                    max_dist = j-i
                    max_i,max_j = i, j

                break
seats[(max_i+max_j)//2]='1'

a2 = get_min_dist(seats) if max_i != -1 or max_j != -1 else -1

#print(a1,a2)
print(max(a1,a2))