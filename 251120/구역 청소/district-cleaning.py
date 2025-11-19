a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.

#겹치는 경우와 겹치지 않는 경우를 나누어 계산한다

#1. 겹치지 않는 경우 : 각 선분의 길이 합
#2. 겹치는 경우 : 가장큰값 - 가장 작은값
if b<c or d<a: 
    print((d-c)+(b-a))
else:
    print(max(a,b,c,d) - min(a,b,c,d))