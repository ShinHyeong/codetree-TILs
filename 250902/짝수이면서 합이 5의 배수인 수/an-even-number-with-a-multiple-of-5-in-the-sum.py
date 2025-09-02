n = int(input())

# Please write your code here.
# n이 짝수인지 확인하는 함수 작성
def is_even(n):
    return n%2==0
# 각자리 숫자합이 5의 배수인지 확인하는 함수 작성
def multiple_5(n):
    sum_val = (n%10)+(n- n%10)//10
    #print(sum_val)
    return sum_val%5==0

#if 문에 함수 넣고 print
if is_even(n) and multiple_5(n):
    print("Yes")
else:
    print("No")