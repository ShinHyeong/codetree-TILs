n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_length=0
curr_seq_length=0

for i in range(n): #idx=0부터 n-1까지 돌면서
    if arr[i] > t: #현재 원소 > T인 경우
        curr_seq_length += 1
    else: #현재 원소가 <= T인 경우
        curr_seq_length = 0
    
    #최대길이 업데이트    
    max_length = max(curr_seq_length, max_length)

print(max_length)