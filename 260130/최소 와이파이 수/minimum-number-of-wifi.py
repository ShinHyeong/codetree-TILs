n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

## 요구사항 분석 ##
# 모든 사람이 사용할 수 있도록 와이파이 최소한으로 설치
# 와이파이수 리턴

## 예제 분석 & 로직 설정 ##
#   v     v   
# 1 1 0 1 1 1
#   v           v
# 1 1 1 0 0 0 1 1 1
# m=1이라면 자신을 포함해 양옆 1+1명까지 커버가능 (=3명)
# 즉 1+m+m명까지 커버 가능하다는 것이다
# 일단 앞에서부터 (1+m+m)명을 봤을 때, 1이 하나라도 있으면 카운팅해야함

answer = 0

group_cnt = 1+m+m
start_idx = 0

while True:
    if group_cnt > n:
        answer += 1
        break

    for i in range(start_idx, start_idx+group_cnt):
        if arr[i]==1:
            answer += 1
            break

    start_idx += group_cnt 

    if n > start_idx >= (n-group_cnt): 
        answer += 1
        break

print(answer)