a, b = map(int, input().split())
n = input()

# Please write your code here.
# a진수 -> b진수 : a진수를 10진수로 바꾸고 이를 b진수로 바꿈
# 8진수 11 -> 2진수 ? 1001
# 8^1 * 1 + 8^0 * 1 = 8 + 1 = 9

# a진수인 n의 각 숫자를 저장하는 리스트를 만듦
binary = list(map(int,n))

# a진수 n -> 10진수 num으로 변환
num=0
for i in range(len(binary)):
    num = num * a + binary[i]

#10진수 num -> b진수로 변환
digits = []
while True :
    if num < b:
        digits.append(num)
        break
    
    digits.append(num % b)
    num //= b

for digit in digits[::-1]:
    print(digit,end='')