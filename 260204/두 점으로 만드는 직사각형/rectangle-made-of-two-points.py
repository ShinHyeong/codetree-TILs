x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.
# 왼쪽하단점과 오른쪽 상단점이 주어진다
# 왼쪽상단점(x3,y3,a3,b3)과 오른쪽 상단점(x4,y4,a4,b4)도 구해본다
x3,y3,x4,y4 = x1,y2,x2,y1
a3,b3,a4,b4 = a1,b2,a2,b1

# 높이 : 8가지 점 중 가장 높은 점과 낮은 점을 구해서 차를 구한다.
h = max(y1,y2,y3,y4,b1,b2,b3,b4)-min(y1,y2,y3,y4,b1,b2,b3,b4)
# 너비 : 8가지 점 중 가장 오른쪽 점과 왼쪽 점을 구해서 차를 구한다.
w = max(x1,x2,x3,x4,a1,a2,a3,a4)-min(x1,x2,x3,x4,a1,a2,a3,a4)

# 넓이 = 높이 * 너비
print(h*w)