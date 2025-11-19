a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.

#겹치는 경우와 겹치지 않는 경우를 나누어 계산한다

#1. 겹치지 않는 경우 : (d-c)+(b-a)
#2. 겹치는 경우
#1) 맨앞이 a, 맨뒤가 d : d-a
#2) 맨앞이 a, 맨뒤가 b : b-a
#3) 맨앞이 c, 맨뒤가 b : b-c
if b<c or d<a: 
    print((d-c)+(b-a))
else:
    if a<=c and c<=b and b<=d:
        print(d-a)
    if a<=c and d<=b:
        print(b-a)
    if c<=a and a<=d and d<=b:
        print(b-c)