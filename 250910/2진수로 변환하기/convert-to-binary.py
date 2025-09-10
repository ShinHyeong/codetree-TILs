n = int(input())

# Please write your code here.
#이진수 : 2로 계속 나누다가 나머지가 2보다 작으면, 
#마지막으로 구한 나머지부터 그동안 나온 나머지들을 거꾸로 이어붙임

digits = [] #나머지를 저장하는 리스트

while True:
    #종료조건 : 나머지가 2보다 작으면 마지막 나머지 저장하고 종료
    if n < 2:
        digits.append(n)
        break

    digits.append(n % 2) #2로 나눈 나머지 저장
    n //= 2#2로 계속 나눔

#마지막으로 구한 나머지부터 그동안 나온 나머지들을 거꾸로 이어붙임
for digit in digits[::-1]:
    print(digit,end='')