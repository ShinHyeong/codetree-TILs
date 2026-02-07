n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
x1_list, x2_list = [],[]
for (x1,x2) in segments:
    x1_list.append(x1)
    x2_list.append(x2)

# N개의 선분 중 1개를 제거해서 나머지를 모두 포함하는 최소 길이의 선분을 구하자
# 가장 작은 시작점(x1)을 가지고 있거나
# 가장 큰 끝점(x2)을 가지고 있는 선분 둘중 하나를 빼자

# 가장 작은 시작점 가진 선분을 제거했을 때, 나머지를 모두 포함하는 선분의 길이
min_x1 = min(x1_list)
min_start, max_end = 100,1
for (x1,x2) in segments:
    if x1 == min_x1:
        continue
    min_start = min(x1, min_start) 
    max_end = max(x2, max_end)
l1 = max_end - min_start

# 가장 큰 끝점 가진 선분을 제거했을 때, 나머지를 모두 포함하는 선분의 길이
max_x2 = max(x2_list)
min_start, max_end = 100,1
for (x1,x2) in segments:
    if x2 == max_x2:
        continue
    min_start = min(x1, min_start) 
    max_end = max(x2, max_end)
l2 = max_end - min_start

# 둘 중 최솟값이 답
print(min(l1,l2))