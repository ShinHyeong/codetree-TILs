a = input()

# Please write your code here.
# 양수 n을 2진법
# 그중 하나만 바꾼 숫자가 a
# n의 후보 -> 십진수

a = list(map(int,a)) #int로 이루어진 문자열로 변환

## 로직 ##
# 1. a의 숫자 하나씩 바꿔보고
# 2. 이를 십진수로 바꾼다
# ex. 110 -> 1*(2**2) + 1*(2**1) + 0*(2**0)
# 3. 최댓값인지 확인한다


max_val = 0
for i in range(len(a)):
    #a의 복사본 사용하여 초기화
    na = a.copy()
    
    #XOR 1 연산 : 0->1, 1->0
    na[i] = na[i]^1 
    
    #십진수로 바꾼다
    sum_val = 0
    for i in range(len(na)):
        sum_val += na[i]*(2**(len(na)-1-i))

    #최댓값인지 확인
    max_val = max(sum_val, max_val)

    
print(max_val)