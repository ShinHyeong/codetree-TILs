N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

# 최댓값과 최솟값의 차 구하는 문제 -> 최솟값를 고정시킨다
# 최솟값이 a라고 할 때, 뽑은 숫자의 범위 : [a:a+k]

max_pick_cnt = 0
for min_val in range(min(arr), max(arr)+1): #최솟값 고정
    pick_cnt = 0
    for pick in arr:
        if (min_val<=pick and pick<=min_val+K):
            pick_cnt+=1
    max_pick_cnt = max(max_pick_cnt, pick_cnt)
print(max_pick_cnt)