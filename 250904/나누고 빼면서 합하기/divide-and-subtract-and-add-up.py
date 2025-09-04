n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def process(m):
    sum_val=0
    while m>=1: #M이 1이 될떄까지
        sum_val += A[m-1] #A의 M번째 원소를 계속더하는데
        if m%2!=0: #M=홀수면 M에서 1을 뺴고
            m-=1
        else: #M=짝수면 M에서 2을 나누고
            m//=2
    return sum_val
print(process(m))