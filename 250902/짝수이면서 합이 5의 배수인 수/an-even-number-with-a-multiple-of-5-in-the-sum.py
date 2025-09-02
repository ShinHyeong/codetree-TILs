n = int(input())

# Please write your code here.
# 각자리 숫자합이 5의 배수인지 확인하는 함수 작성
def multiple_5(n):
    sum_val = n%10+(n-n%10)
    return sum_val%5==0

#if 문에 함수 넣고 print
if multiple_5:
    print("Yes")
else:
    print("No")