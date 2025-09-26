N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
min_val = 10000

#제외할 숫자 2개 선택
for e1 in range(N-1):
    for e2 in range(e1+1,N):
        
        sum_val=0        
        #전체 숫자 중에
        for i in range(N):    
            if i==e1 or i==e2:
                continue
            sum_val += arr[i] #제외한 n-2개의 숫자들의 합 구하기
    
        #s와 (그 합의 차) 최솟값 구하기
        min_val = min(abs(S-sum_val),min_val)

#출력
print(min_val)