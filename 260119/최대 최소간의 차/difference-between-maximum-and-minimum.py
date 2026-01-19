n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

# 모든 구간의 수의 범위 : 1이상 10000 이하로 매우작음
# 모든 수는 [x, x+k] 여야함
# x를 1부터 10000까지 다 움직여보며
# 모든 수를 그 구간안에 끼워넣었을 때의 비용을 구한다
# 그중 최소를 리턴한다

# [x,x+k] 사이로 바꾸는 cost를 계산한다
def get_cost(low, high):
    cost = 0
    for ele in arr:
        if ele < low:
            cost += (low-ele)
        if ele > high:
            cost += (ele-high)
    
    return cost

# 모든 구간별 비용을 구해보며 그 중 최솟값을 계산한다
min_cost = 10000 * 100

for num in range(1,10000+1):
    min_cost = min(min_cost, get_cost(num,num+k))

print(min_cost)