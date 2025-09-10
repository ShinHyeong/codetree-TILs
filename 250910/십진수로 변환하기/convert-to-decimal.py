binary = input()

# Please write your code here.
binary = list(map(int,binary)) #이진수를 숫자로된 리스트로 저장
num = 0 #십진수는 0으로 초기화

for i in range(len(binary)):
    num = num * 2 + binary[i] #이진수 -> 십진수 점화식

print(num) #십진수 출력