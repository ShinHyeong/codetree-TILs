x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.
#겹치지 않는경우 : 1)y2<a1 2) a2<x1 3) b2<y1 3) y2<b1
print("nonoverlapping" if y2<a1 or a2<x1 or b2<y1 or y2<b1 else "overlapping")