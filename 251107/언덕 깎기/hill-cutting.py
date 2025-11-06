N = int(input())
heights = [int(input()) for _ in range(N)]

# Please write your code here.
MAX_H = 100
min_cost = MAX_H * MAX_H

for i in range(N): #최솟값 고정
    
    cost = 0

    for j in range(N):
        if heights[i]==heights[j]:
            x=0

        if heights[j]<=heights[i]:
            x = heights[i]-heights[j] #h_i를 최솟값으로 만들어야함 : h_j+x = h_i

        if heights[j]>heights[i]:
            if abs(heights[j]-heights[i])<=17:
                x=0

            if heights[j]>heights[i]+17: #마지노선보다 크다면 최댓값이 마지노선이 되어야하므로
                x = heights[j]-(heights[i]+17) #h_j - x = h_i+17 
        
        cost += x*x #비용계산
    
    min_cost = min(cost, min_cost) #최소비용인지 확인

print(min_cost)
