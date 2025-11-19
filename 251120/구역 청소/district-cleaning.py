a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.

#겹치는 경우와 겹치지 않는 경우를 나누어 계산한다

#1. 겹치지 않는 경우 : (d-c)+(b-a)
#2. 겹치는 경우
#1) c<=b and b<=d
#2) a<=c and c<=b

if b<c or d<a: 
    print((d-c)+(b-a))
else:
    if c<=b and b<=d:
        print(d-a)
    else:
        print(b-c)