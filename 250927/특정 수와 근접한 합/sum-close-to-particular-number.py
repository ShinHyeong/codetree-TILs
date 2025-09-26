N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
min_val = 10000

#제외할 숫자 2개 선택
for e1 in range(N-1):
    for e2 in range(e1+1,N):
        
        # e1번과 e2번을 제외한 나머지 숫자의 총합
        sum_val = sum(arr)-arr[e1]-arr[e2] 
           
        #s와 (그 합의 차) 최솟값 구하기
        min_val = min(abs(S-sum_val),min_val)

#출력
print(min_val)