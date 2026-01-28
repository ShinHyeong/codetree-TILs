n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
## 요구사항 분석
# n개의 수 중 3개의 수 골라서 나올 수 있는 최댓값 구하기

## 예제 분석
# 10 -5 -2 4 -9 15 -3 6 0 7 1 -20 (총 12개의 수)

# 로직설정
# 양수갯수,음수갯수
# 3,0 = 곱했을 때 값이 양수이므로 절댓값이 큰 값 고르기
# 2,1 = 곱했을 때 값이 음수이므로 절댓값이 작은 값 고르기
# 1,2 = 곱했을 때 값이 양수이므로 절댓값이 큰 값 고르기
# 0,3 = 곱했을 때 값이 음수이므로 절댓값이 작은 값 고르기
# 세가지 수 중 하나라도 0이 있는 경우

# 2가지 케이스 중 가장 큰 값 선택
MAX_MULTI = 1000*1000*1000
v1, v2, v3 = -MAX_MULTI,-MAX_MULTI, -MAX_MULTI

for ele in arr:
    if ele==0:
        v3 = 0

# 절댓값을 기준으로 배열을 재정렬한다
arr.sort(key=lambda x:abs(x))

# 뒤에서부터 3가지 수를 구한다. 단 모두 곱했을 때 양수여야한다.

for i in range(n-1,-1,-1):
    for j in range(i-1,-1,-1):
        for k in range(j-1,-1,-1):
            if arr[i]*arr[j]*arr[k] <= 0:
                continue
            v1 = arr[i]*arr[j]*arr[k]
            break
        break
    break

# 앞에서부터 3가지 수를 구한다. 단 모두 곱했을 때 음수여야한다.
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]*arr[j]*arr[k] >= 0:
                continue
            v2 = arr[i]*arr[j]*arr[k]
            break
        break
    break

print(max(v1,v2,v3))
