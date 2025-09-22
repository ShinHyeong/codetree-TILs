a = input()

# Please write your code here.
# 양수 n을 2진법
# 그중 하나만 바꾼 숫자가 a
# n의 후보 -> 십진수

a = list(map(int,a)) #int로 이루어진 문자열로 변환

## 로직 ##
# 1. 앞에서부터(idx=0) 하나씩 꺼내서 가장 앞에 있는 0을 1로 바꿔준다
# 2. 이를 십진수로 바꾼다
# ex. 110 -> 1*(2**2) + 1*(2**1) + 0*(2**0)

for i in range(len(a)):
    if a[i]==0:
        a[i] = 1
        break

sum_val=0
for i in range(len(a)):
    sum_val += a[i]*(2**(len(a)-1-i))

print(sum_val)