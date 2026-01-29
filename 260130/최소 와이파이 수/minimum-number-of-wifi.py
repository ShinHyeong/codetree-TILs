n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

## 요구사항 분석 ##
# 모든 사람이 사용할 수 있도록 와이파이 최소한으로 설치
# 와이파이수 리턴

## 예제 분석 & 로직 설정 ##
#   v     v   
# 1 1 0 1 1 1
# m=1이라면 자신을 포함해 양옆 1+1명까지 커버가능 (=3명)
# 즉 1+m+m명까지 커버 가능하다는 것이다
# 따라서 n//(1+m+m) 하면 될듯
# 만약 나누어떨어지지 않으면 (n//(1+m+m)) + 1
people_cnt = 0
for ele in arr:
    if ele == 1:
        people_cnt +=1

#answer= n//(1+m+m)
#if n%(1+m+m)!=0:
#    answer = (n//(1+m+m)) + 1

answer= people_cnt//(1+m+m)
if people_cnt%(1+m+m)!=0:
    answer = (people_cnt//(1+m+m)) + 1
print(answer)