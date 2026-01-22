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

first_seat_idx = 0
for i in range(len(seats)):
    if seats[i]=='1':
        first_seat_idx = i
        break

dist_list = []
dist = 1
for i in range(first_seat_idx+1,len(seats)):
    if seats[i]=='1':
        dist_list.append(dist)
        dist = 0
    dist += 1

max_dist = max(dist_list)
dist = 0
target_idx1, target_idx2 = 0,0
for i in range(len(seats)):
    if seats[i]=='1':
        if dist==max_dist:
            target_idx2 = i
            target_idx1 = i-max_dist
            break
        dist=0
    dist += 1

seats_list = list(seats)
x_idx = (target_idx1 + target_idx2)//2
seats_list[x_idx] = '1'
seats = "".join(seats_list)

dist_list = []
dist = 1
for i in range(first_seat_idx+1,len(seats)):
    if seats[i]=='1':
        dist_list.append(dist)
        dist = 0
    dist += 1
print(min(dist_list))