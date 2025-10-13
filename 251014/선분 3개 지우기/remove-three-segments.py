n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

# Please write your code here.

#서로 다른 선분 3개를 골라서 그 선분을 제외하고 그린다
#남은 n-3개의 선분끼리 서로 겹치지 않는지 확인한다
    #겹치지 않는다면 카운팅
cnt=0 
for l1_idx in range(n): #서로 다른 선분 3개 고르기
    for l2_idx in range(l1_idx+1, n):
        for l3_idx in range(l2_idx+1, n):
            
            MAX_INT = 100
            arr = [0] * (MAX_INT+1)

            for i in range(len(l)):
                if i==l1_idx or i==l2_idx or i==l3_idx: #그 선분을 제외하고 그린다
                    continue

                left,right = l[i], r[i]
                for k in range(left, right+1):
                    arr[k] += 1

            overlap = False
            for i in range(len(arr)):
                if arr[i]>1: #한번이라도 겹치면 True
                    overlap = True
            if overlap == False:
                cnt+=1
print(cnt)