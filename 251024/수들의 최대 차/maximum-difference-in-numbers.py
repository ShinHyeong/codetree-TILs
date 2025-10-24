N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

# 최댓값과 최솟값의 차 구하는 문제 -> 최솟값를 고정시킨다
# 최솟값이 a라고 할 때, 뽑은 숫자의 범위 : [a:a+k]

max_cnt = 0
for min_val in range(min(arr), max(arr)+1): #최솟값 고정
    cnt = 0
    for elm in arr: #조건을 만족하는 숫자 갯수를 센다
        if (min_val<=elm and elm<=min_val+K): 
            cnt+=1
    max_cnt = max(max_cnt, cnt) #조건을 만족하는 숫자 갯수가 최댓값인지 확인한다
print(max_cnt)