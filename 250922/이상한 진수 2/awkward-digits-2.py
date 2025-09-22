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
# 예외 : 만약 전부 1로만 채워지는 경우도 있으니
# 그렇다면 가장 뒤에 있는 1을 0으로 바꿔준다

# 0이 존재하는가? 존재한다면 가장 앞에 있는 인덱스를 리턴하고 아니라면 -1을 리턴한다
def pos_zero(a):
    for i in range(len(a)):
        if a[i]==0:
            return i
    return -1
    
if pos_zero(a)>=0:
    a[pos_zero(a)]=1
else :
    for i in range(len(a)-1, -1):
        if a[i]==1:
            a[i]=0
            break

sum_val=0
for i in range(len(a)):
    sum_val += a[i]*(2**(len(a)-1-i))

print(sum_val)