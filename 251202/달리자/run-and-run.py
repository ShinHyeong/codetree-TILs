n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

# 1번 집부터 보면서 남으면 가장 가까운 부족한 집에게 나눠준다

dst = 0
for i in range(n):
    if A[i]>B[i]: #남는집이라면
        for j in range(i+1,n): 
            if A[j]<B[j]: #부족한 집을 찾아
                #부족한 만큼 나눠준다
                #그런데 만약 부족한 양 >= 남는 양이라면 남는 양을 전부줘야한다
                if B[j]-A[j] >= A[i]-B[i]:
                    give = A[i]-B[i]
                    A[i] -= give
                    A[j] += give
                    dst += (give) * (j-i)
                #남는양 > 부족한 양이라면 부족한 양만큼만 주면 된다
                else:
                    give = B[j]-A[j]
                    A[i] -= give
                    A[j] += give
                    dst += (give) * (j-i)
print(dst)