import sys
n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
min_val = sys.maxsize
for i in range(n): #모이는 집 i
    sum_val = 0
    for j in range(n): #1번째 집 주민부터 ~ n번째 집 주민까지 이동한다.
        sum_val += A[j] * abs(i-j) #사람수 * 거리(=인덱스 간의 차)
    if sum_val < min_val:
        min_val = sum_val
print(min_val)