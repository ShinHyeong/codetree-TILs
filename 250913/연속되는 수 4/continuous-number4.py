n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
# 증가하는 연속부분수열 중 최대길이
max_len = 0
# 현재 카운팅하는 증가하는 연속부분수열 길이
curr_len = 0

for i in range(n):
    if i>=1 and arr[i] > arr[i-1]:
        curr_len += 1
    else: #i==0 또는 증가하지 않는 경우는 새로운 카운트이므로 1로 처리
        curr_len = 1
    
    max_len = max(curr_len, max_len)

print(max_len)