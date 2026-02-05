x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.
# 각 사각형별로 왼쪽하단, 우측상단 좌표가 주어진다
# 이를 통해 왼쪽상단, 우측하단 좌표를 구할 수 있다
x3,y3,x4,y4 = x1,y2,x2,y1
a3,b3,a4,b4 = a1,b2,a2,b1

# 너비 = x좌표 최댓값 - x좌표 최솟값
w = max(a1,a2,a3,a4,x1,x2,x3,x4) - min(a1,a2,a3,a4,x1,x2,x3,x4)
# 높이 = y좌표 최댓값 - y좌표 최솟값
h = max(b1,b2,b3,b4,y1,y2,y3,y4) - min(b1,b2,b3,b4,y1,y2,y3,y4)

# 너비와 높이 중 더 큰 것을 고르고 이를 정사각형의 변으로 삼는다
print(max(w,h)*max(w,h))