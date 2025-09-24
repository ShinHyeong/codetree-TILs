import sys
n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.

#room_idx :a[room_idx]
# 1번 : 4명 -> 4*abs(1-2)
# 2번 : 7명 -> 7*abs(2-2)
# 3번 : 8명 -> 8*abs(3-2)
# 4번 : 6명 -> 6*abs(4-2) 
# 5번 : 4명 -> 4*abs(5-2)
# 거리의 합 : a[room_idx-1]*abs(room_idx-start_idx)

#어떤 방에서 시작해야 각 방에 정해진 인원이 들어가는데까지의 거리의 합을 최소화할 수 있는지
min_dist = sys.maxsize
for start_idx in range(n): #시작하는 방 하나 정하고
    #거리 계산
    dist=0
    for room_idx in range(n):
        dist += a[room_idx-1]*abs(room_idx-start_idx)
    
    #최소값 계산
    min_dist=min(dist,min_dist)

print(min_dist)