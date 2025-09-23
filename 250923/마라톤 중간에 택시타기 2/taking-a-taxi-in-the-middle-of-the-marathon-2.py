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
for pass_idx in range(1,n-1): #건너뛸 체크포인트 idx:0~n-2

    #건너뛸 체크포인트를 제외한 모든 거리
    curr_dist = 0
    prev_idx = 0 # 0부터 시작해서
    for i in range(1, n): #idx:1~n-1 
        #pass_idx==i -> [i-1번째 체크포인트 ~ i+1번째 체크포인트] 거리 계산
        if i==pass_idx: #만약 다음체크포인트가 건너뛸 체크포인트라면 체크포인트 다음으로 넘기고
            continue 
        curr_dist += abs(x[prev_idx]-x[i]) + abs(y[prev_idx]-y[i])  #거리계산
        prev_idx = i #그 다음 포인트로 옮겨주고

    #최솟값인지 ?
    min_dist = min(curr_dist, min_dist) 

print(min_dist)