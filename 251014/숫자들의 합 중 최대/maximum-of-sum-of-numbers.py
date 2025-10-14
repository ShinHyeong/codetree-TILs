X, Y = map(int, input().split())

# Please write your code here.
#각자리 숫자 구하기
def get_num(num):
    digits = []
    while num>=10:
        digits.append(num%10)
        num //= 10
    digits.append(num%10)
    return digits[::-1]

max_val = 0
for i in range(X,Y+1):
    sum_val = sum(get_num(i))
    max_val = max(sum_val,max_val)
print(max_val)