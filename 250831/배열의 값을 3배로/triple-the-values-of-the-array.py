#배열 입력받기
arr_2d = [
    list(map(int, input().split()))
    for _ in range(3)
]

#모든 요소 돌면서#3배로 바꾸기
#배열 다시 출력
for i in range(3):
    for j in range(3):
        arr_2d[i][j]*=3
        print(arr_2d[i][j], end=" ")
    print()

