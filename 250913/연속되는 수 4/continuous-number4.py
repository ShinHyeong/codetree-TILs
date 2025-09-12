n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
# 증가하는 연속 부분 수열 길이를 저장하는 리스트
# 증가하는 연속부분수열 : 연속부분수열 중 원소의 숫자가 계속 커지는 수열을 의미함
inc_seq_lengths = []

#현재 증가하는 연속부분 수열의 길이
cnt = 1
# 증가하는지 어떻게 판단? 현재원소 > 직전원소
for i in range(1,n):
    if arr[i] > arr[i-1] : #증가하는 연속부분 수열이다
        cnt+=1
    else: #아니다
        inc_seq_lengths.append(cnt)
        cnt=1
#마지막 연속부분 수열 길이 추가
inc_seq_lengths.append(cnt)

# 증가하는 연속 부분 수열 중 최대길이 출력
print(max(inc_seq_lengths))