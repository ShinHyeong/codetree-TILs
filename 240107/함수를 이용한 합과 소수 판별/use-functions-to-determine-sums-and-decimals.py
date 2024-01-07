a,b=map(int,input().split())

def is_prime(n):
    if n==1:
        return True
    for i in range(2, n):
        if n%i==0:
            return False
    return True

def is_digit_sum_even(n):
    digit_sum = (n//100) + (n//10) + (n%10)
    return (digit_sum%2==0)

def cnt_odd(a,b):
    cnt=0
    for i in range(a,b+1):
        if is_prime(i) and is_digit_sum_even(i):
            cnt+=1
    return cnt
print(cnt_odd(a,b))