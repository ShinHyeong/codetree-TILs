N = int(input())
seats = input()

# Please write your code here.

##요구사항 분석
# 1명 더 집어넣었을 때, 가장 가까운 간격(최소거리)을 최대로 하고 싶음

##예제 분석
# 총 12자리
# 100010010001 -> 가장 가까운 간격 : 3
# 10x010010001 -> 가장 가까운 간격 : 2
# 100010010x01 -> 가장 가까운 간격 : 2
 
##로직 : 가장 넓은 간격의 가운데를 고르고 그 거리를 구한다
# 1. 가장 넓은 간격을 찾는다
# 2. 그 간격의 가운데 idx를 찾고, x를 넣는다
# 3. 가장 가까운 간격을 구한다

seats = list(seats)
max_dist = 0
max_i, max_j = -1,-1
for i in range(N):
    if seats[i]=='1':
        for j in range(i+1,N):
            if seats[j]=='1':
                # '1'간의 쌍을 구했을 때 최대 간격 업데이트
                if j-i > max_dist:
                    max_dist = j-i
                    max_i, max_j = i,j
                
                # '1'간의 쌍을 구했으므로 for j문 종료
                break

seats[(max_i+max_j)//2] = '1'

min_dist = 1000
for i in range(N):
    if seats[i]=='1':
        for j in range(i+1,N):
            if seats[j]=='1':
                # '1'간의 쌍을 구했을 때 최소 간격 업데이트
                if j-i < min_dist:
                    min_dist = j-i
                # '1'간의 쌍을 구했으므로 for j문 종료
                break
print(min_dist)