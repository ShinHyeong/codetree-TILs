x1, x2, x3, x4 = map(int, input().split())

# Please write your code here.

#겹치지 않는 경우
# (x1,x2) 가 (x3,x4)를 앞선 경우 : x2 < x3
# (x3,x4)가 (x1,x2)를 앞선 경우 : x4 < x1

print("nonintersecting" if x2 < x3 or x4 < x1 else "intersecting")