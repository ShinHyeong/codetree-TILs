N = int(input())
seat = input()

# Please write your code here.
seat = list(map(int,seat))

max_val = 0
#가장 가까운 거리에 대해 가능한 모든 조합을 만들어 확인한다

for target in range(N):
    if seat[target]==1:
        continue
    
    seat[target] = 1 #빈 좌석이면 한번 사람을 둬본다
    
    min_dist = N #가장 가까운 두 사람의 거리를 구한다
    for i in range(N):
        for j in range(i+1, N):
            if seat[i]==1 and seat[j]==1:
                dist = j-i
                min_dist = min(dist, min_dist)

    max_val = max(max_val, min_dist) #가장 가까운 두 사람의 거리의 최댓값인지 확인
    seat[target] = 0 #자리 원상복귀
    
print(max_val)