import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
#거리
def get_dist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

min_dist = sys.maxsize 
for pass_idx in range(1,n-1): #건너뛸 체크포인트
    points_cpy = points.copy()
    points_cpy.pop(pass_idx)

    curr_dist = 0
    for i in range(len(points_cpy)-1):
        x1,y1 = points_cpy[i][0],points_cpy[i][1]
        x2,y2 = points_cpy[i+1][0],points_cpy[i+1][1]
        curr_dist += get_dist(x1,y1,x2,y2)

    min_dist = min(curr_dist, min_dist) 

print(min_dist)