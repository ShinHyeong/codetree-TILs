#배열1 입력받기
#배열2 입력받기
arr_1 = [list(map(int,input().split())) for _ in range(3)]
input()
arr_2 = [list(map(int,input().split())) for _ in range(3)]

arr_3 = [[0 for _ in range(3)] for _ in range(3)]
#배열포맷만큼 돌면서
#같은위치 곱하기
#출력
for i in range(3):
    for j in range(3):
        arr_3[i][j] = arr_1[i][j] * arr_2[i][j]
        print(arr_3[i][j], end=" ")
    print()