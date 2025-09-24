import sys
n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.

#room_idx :a[room_idx] -> a[room_idx]*(i-n)
# 3번 : 6명 -> 6*(3-3) 
# 4번 : 4명 -> 4*(4-3)
# 0번 : 4명 -> 4*(5-3) #n=5
# 1번 : 7명 -> 7*(6-3) #n=5
# 2번 : 8명 -> 8*(7-3) #n=5

#어떤 방에서 시작해야 각 방에 정해진 인원이 들어가는데까지의 거리의 합을 최소화할 수 있는지
min_dist = sys.maxsize
for start_idx in range(n): #시작하는 방 하나 정하고
    
    #거리 계산
    dist=0
    for i in range(start_idx, start_idx+n):
        room_idx = i-n if i>n-1 else i
        dist += a[room_idx]*(i-start_idx)
    
    #최소값 계산
    min_dist=min(dist,min_dist)

print(min_dist)