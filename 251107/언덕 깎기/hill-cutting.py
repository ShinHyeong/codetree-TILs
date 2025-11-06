N = int(input())
heights = [int(input()) for _ in range(N)]

# Please write your code here.
MIN_H,MAX_H = 1,100
min_cost = (MAX_H-MIN_H)*(MAX_H-MIN_H)*N

for h in range(MIN_H,MAX_H+1): #최솟값 고정
    
    cost = 0

    for j in range(N):


        if heights[j]<h:
            cost += (h-heights[j]) * (h-heights[j]) #h를 최솟값으로 만들어야함 : h_j+x = h

        if heights[j]>h+17: #마지노선보다 크다면 최댓값이 마지노선이 되어야하므로
            cost += (heights[j]-(h+17)) * (heights[j]-(h+17)) #h_j - x = h+17 
        
    
    min_cost = min(cost, min_cost) #최소비용인지 확인

print(min_cost)
