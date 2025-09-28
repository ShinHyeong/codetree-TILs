n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
# 구간 하나씩 잡아본다
max_val = 0
for start_idx in range(n-k+1): # 구간 시작값 : 0~n-k
    sum_val = sum(arr[start_idx:start_idx+k]) #start_idx ~ start_idx+(k-1)의 합
    max_val = max(sum_val, max_val)
print(max_val)