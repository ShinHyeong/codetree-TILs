x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.
# 다른쪽의 꼭짓점도 구한다
x3,y3,x4,y4 = x1,y2,x2,y1
a3,b3,a4,b4 = a1,b2,a2,b1 

c1,d1,c2,d2 = -1,-1,-1,-1
# x3과 a3 중 어떤 게 더 작은지(더 왼쪽에 위치한지) 구한다
    # x3이 더 왼쪽에 위치한다면, 최소 직사각형의 꼭짓점은 (x3,y3)
    # 그게 아니라면, 최소 직사각형의 꼭짓점은 (a3,b3)
if x3<=a3:
    c1,d1 = x3,y3
else:
    c1,d1 = a3,b3

# x4와 a4 중 어떤 게 더 큰지(더 오른쪽에 위치한지) 구한다
    # x4가 더 오른쪽에 위치한다면, 최소 직사각형의 꼭짓점은 (x4,y4)
    # 그게 아니라면, 최소 직사각형의 꼭짓점은 (a4,b4)
if x4>=a4:
    c2,d2 = x4,y4
else:
    c2,d2 = a4,b4

print((c2-c1)*(d1-d2))