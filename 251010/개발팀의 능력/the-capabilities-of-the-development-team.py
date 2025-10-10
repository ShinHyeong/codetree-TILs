arr = list(map(int, input().split()))

# Please write your code here.

min_val = 1000
for a1 in range(len(arr)):
    for a2 in range(a1+1, len(arr)):
        
        for a3 in range(len(arr)):
            for a4 in range(a3+1, len(arr)):
                
                if not(a1!=a3 and a1!=a4 and a2!=a3 and a2!=a4): #필수전제조건 : 팀원은 모두 인덱스가 다르다 
                    continue
                
                sum1 = arr[a1]+arr[a2]
                sum2 = arr[a3]+arr[a4]
                sum3 = sum(arr)-sum1-sum2

                if sum1==sum2 or sum2==sum3 or sum1==sum3: #모든 팀의 능력치는 서로 다르게 묶여야함
                    continue

                diff = max(sum1, sum2, sum3) - min(sum1, sum2, sum3)

                min_val = min(diff, min_val)

print(-1 if min_val==1000 else min_val) #min_val이 초기화값이라면 모든 팀의 능력치가 서로 다르지 묶어야한다는 조건을 통과하지 못한거임
