from functools import cmp_to_key

n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.
# 원점 (0,0)과 주어진 점(x,y) 사이 멘하턴 거리를 구하는 함수
def dist(x, y):
    dist_x = x if x>=0 else -x
    dist_y = y if y>=0 else -y
    return dist_x + dist_y

# 커스텀 우선순위 대로 정렬 (멘하턴 거리 오름차순 -> 번호 오름차순)
points.sort(key=lambda p : (dist(p[1][0],p[1][1]), p[0]))

# 점의 번호 출력
for (number, _) in points:
    print(number+1)