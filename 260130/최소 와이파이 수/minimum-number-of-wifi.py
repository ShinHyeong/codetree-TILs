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
# 1을 마주하면 cnt+=1
    # 그 다음부터 검사할 인덱스는 1+m+m부터 시작
# 0을 마주하면 패스하고 다음칸으로 옮기면서 검사
# 종료조건 i>=n-group_cnt

cnt=0

group_cnt = 1+m+m
i = 0
while True:
    if i >= (n-group_cnt): #종료조건
        for j in range(i,n):
            if arr[j]==1:
                cnt+=1
                break
        break

    if arr[i]==0:
        i+=1
    else: #arr[i]==1
        cnt+=1
        i+=(1+m+m)

print(cnt)
