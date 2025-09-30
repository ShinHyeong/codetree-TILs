N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
# 길이가 m인 a의 부분이 b의 원소 순서 바꾼거에 해당하는지
# 1. 길이가 m인 a의 부분 만들기
# 2. b의 원소 모두 통과하는지 -> 하나라도 아니라면 false
    # 카운팅
#3. 카운팅 값 출력

cnt=0
for start_idx in range(N-M+1): #시작인덱스값 : 0 ~ (n-m)
        part = A[start_idx:start_idx+M]
        
        isValid = True
        for p in part:
            if not p in B:
                isValid = False
        if isValid:
            cnt+=1

print(cnt)