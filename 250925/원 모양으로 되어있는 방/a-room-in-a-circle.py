import sys
n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.

# 조건분기로 해결해볼까?
# (1) 도착지 >= 시작지: dist = 도착지 - 시작지 
# (2) 도착지 < 시작지: dist = (도착지 + n) - 시작지
# n : 5
# 시작하는 방(start_idx) : 3번
# 도착지 : 거리
# 3번 : 0 -> dist=0 = 3-3 
# 4번 : 1 -> dist=1 = 4-3
# 0번 : 2 -> dist=2 = (0+5)-3
# 1번 : 3 -> dist=3 = (1+5)-3
# 2번 : 4 -> dist=4 = (2+5)-3

# 조건 분기로 처리하는 대신 모듈러 연산으로 처리하자
# 원형 = 시계 = 모듈러 연산 (%)
# 모듈러 연산의 의미: 돌고 돌아 몇 번째 방?
# (end_idx + n) - start_idx
# : (end_idx에서 돌고 돌아 몇 번째 방) - start_idx


#어떤 방에서 시작해야 각 방에 정해진 인원이 들어가는데까지의 거리의 합을 최소화할 수 있는지
min_dist = sys.maxsize
for start_idx in range(n): #시작하는 방 하나 정하고
    
    for end_idx in range(n): #끝나는 방 하나씩 돌면서 그에 대한 거리합을 구한다 
        dist = (end_idx + n) - start_idx #(end_idx에서 돌고 돌아 몇 번째 방) - start_idx
        sum_dist += a[end_idx] * dist #거리합 = (인원 수) * (방 사이의 거리)
    
    #최소값 계산
    min_dist=min(dist,min_dist)

print(min_dist)