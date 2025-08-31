#4*4개의 정수 입력받기
arr_2d = [list(map(int,input().split())) for _ in range(4)]

#각 줄마다 돌면서
#각줄의 합구하고
#각줄마다출력

for i in range(4):
    total = 0
    for j in range(4):
        total += arr_2d[i][j]
    print(total)