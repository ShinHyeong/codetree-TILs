n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
# T보다 큰 수로만 이루어진 연속 부분 수열의 길이를 저장하는 리스트
over_T_lengths = []

max_length=0
curr_seq_length=1 if arr[0] > t else 0

for i in range(1, n): #idx=1부터 n-1까지 T보다 큰지 검사 
    if arr[i]>t and arr[i-1]>t : #T보다 큰 원소가 연속적이다 (현재원소도 큰데 직전원소도 크다)
        if curr_seq_length==0: #그런데 처음 카운트했다
            curr_seq_length = 1 #1로 초기화 
        curr_seq_length+=1
    else: #그렇지 않다
        if arr[i]>t: #그렇지만 현재 원소는 T보다 크다
            curr_seq_length=1
            max_length = max(curr_seq_length, max_length)
        else:
            max_length = max(curr_seq_length, max_length)
            curr_seq_length=0
max_length = max(curr_seq_length, max_length)
        
print(max_length)