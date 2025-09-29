n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
#구간의 시작점과 끝점을 잡아 완전탐색한다
#평균값을 구한다
#평균값이 그 구간의 원소 중 하나인지 확인한다
    #카운팅한다

cnt=0
for start_idx in range(n):
    for end_idx in range(start_idx+1, n):
        part = arr[start_idx:end_idx+1]
        sum_val = sum(part) 
        avg_val = sum_val//(len(part))
        
        found = False
        for ele in part:
            if ele == avg_val:
                found = True
                break

        if found==True:
            cnt+=1
        
print(cnt)