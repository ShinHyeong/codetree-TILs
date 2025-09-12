N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

# 부호가 동일한 정수로만 이루어진 연속 부분 수열 길이를 저장하는 리스트
same_sign_lengths = []

# 부호가 다르면 리스트에 직전부호 길이를 추가함
cnt = 1 #i=0부터 시작
for i in range(1, N):
    if arr[i]*arr[i-1] < 0: #부호가 다르다
        same_sign_lengths.append(cnt)        
        cnt=1 #현재 부호 수열 길이 초기화
    else : #부호가 같다
        cnt+=1
#마지막 부호 수열 길이 리스트에 추가
same_sign_lengths.append(cnt)

# 부호가 동일한 정수로만 이루어진 연속 부분 수열의 최대길이 출력
print(max(same_sign_lengths))
