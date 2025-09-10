N = input()

# Please write your code here.
binary = list(map(int,N)) #이진수 -> 각 숫자를 저장하는 리스트로 변경

# 이진수 -> 십진수 :현재십진수 = 예전십진수 * 2 + 현재이진수 숫자
num = 0 #현재십진수
for i in range(len(binary)):
    num = num * 2 + binary[i]

# 십진수 * 17로 현재 십진수 업데이트
num = num * 17

# 이를 다시 이진수로 나타내기
digits = []
while True:
    if num < 2:
        digits.append(num)
        break

    digits.append(num % 2)
    num //= 2

for digit in digits[::-1]:
    print(digit,end='')