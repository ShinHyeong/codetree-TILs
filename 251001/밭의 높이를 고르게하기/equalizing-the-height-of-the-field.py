N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
# 최소 T번이상 H 높이로..

# 밭을 돌면서
# T 길이 이상의 구간을 잡는다
# 그 구간을 H로 만드는데 걸리는 비용을 계산한다
    #최소 비용인지 확인한다

min_cost = 100*200
for start in range(N): 
    for end in range(start+T-1,N):

        cost = 0
        for i in range(start,end+1):
            cost += abs(H-arr[i])
        min_cost = min(cost, min_cost)

print(min_cost)