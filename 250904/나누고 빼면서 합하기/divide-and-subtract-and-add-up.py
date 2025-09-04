n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def process(m):
    sum_val=0
    while m>=1:
        #print(m, A[m-1])
        sum_val += A[m-1]
        if m%2!=0:
            m-=1
        else:
            m//=2
    return sum_val
print(process(m))