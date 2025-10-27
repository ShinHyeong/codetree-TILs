N = int(input())
seat = input()
# Please write your code here.

# 2명의 자리 정하기
# 가장 가까운 두 사람의 거리 구하기
# 최댓값인지 확인하기

MAX_N = 100
seat = list(map(int,seat))

def get_min_dist():

    min_dist = MAX_N
    for i in range(N):
        for j in range(i+1, N):
            if seat[i]==1 and seat[j]==1:
                min_dist = min(j-i, min_dist)

    return min_dist

max_val = 0
for i in range(N):
    for j in range(i+1,N):

        #둘중하나라도 앉을수없다면 자리후보탈락
        if seat[i]==1 or seat[j]==1:
            continue
        
        #잠깐 자리 앉히기
        seat[i],seat[j] = 1,1
        
        #가장 가까운 두 사람의 거리 구하기
        min_dist = get_min_dist()
            
        # 최대값인지 확인하기 
        max_val = max(max_val, min_dist)

        #원상복구
        seat[i],seat[j] = 0,0

print(max_val)