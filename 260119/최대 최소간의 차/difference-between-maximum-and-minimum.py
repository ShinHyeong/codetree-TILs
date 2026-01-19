n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

# 6 3 7 3 5 최대 최소 차가 2 이하가 되게
# 현재의 max를 깎거나 현재의 min을 높이거나

def is_diff_LTE_K(arr):
    return max(arr)-min(arr) <= k

def get_min_val_cnt(arr):
    min_val, min_val_cnt = min(arr), 0
    for ele in arr:
        if ele == min_val:
            min_val_cnt += 1
    return min_val_cnt

def get_max_val_cnt(arr):
    max_val, max_val_cnt = max(arr), 0
    for ele in arr:
        if ele == max_val:
            max_val_cnt += 1
    return max_val_cnt

cost = 0
min_val, max_val = min(arr), max(arr)

while not is_diff_LTE_K(arr):
    max_val -= 1
    for i in range(n):
        if arr[i] == max_val+1:
            cost += 1
            arr[i] -= 1

    if is_diff_LTE_K(arr):
        break

    min_val += 1
    for i in range(n):
        if arr[i] == min_val-1:
            cost += 1
            arr[i] += 1
    
print(cost)