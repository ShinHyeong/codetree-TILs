a, b, x, y = map(int, input().split())

# Please write your code here.
# 목표 : A -> B
# 단, x->y 또는 y->x로 순간이동 가능

# ex. A B x y : 3 10 8 2
# 일단 오름차순으로 정렬하면, y A x B (2 3 8 10)
# 방법1. A -> (텔레포트 사용:x -> y) -> B
# 방법2. A -> (텔레포트 사용:y -> x) -> B
# 방법3. A -> B

m1 = abs(x-a) + abs(b-y)
m2 = abs(y-a) + abs(b-x)
m3 = abs(b-a)

print(min(m1,m2,m3))