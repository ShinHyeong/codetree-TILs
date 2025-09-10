N, B = map(int, input().split())

# Please write your code here.
#b진수 : n을 b로 계속 나누다가 나머지가 b보다 작으면 종료하고
#마지막 나머지부터 지금까지 나온 나머지까지 거꾸로 이어붙이기

digits = []
while True:
    if N < B:
        digits.append(N)
        break

    digits.append(N % B)
    N //= B

for digit in digits[::-1]:
    print(digit,end='')