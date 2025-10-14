n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
#등차수열을 이루는지
def is_seq(i,k,j):
    return a[j]-k == k-a[i]

max_val = 0
for k in range(1,100+1):
    cnt=0
    for i in range(n):
        for j in range(i+1,n):
            if is_seq(i,k,j):
                cnt+=1
    max_val = max(cnt,max_val)
print(max_val)