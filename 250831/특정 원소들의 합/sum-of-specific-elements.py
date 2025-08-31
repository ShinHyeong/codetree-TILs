#4x4 배열 입력받기
#배열 전체 돌기
#색칠된 칸의 수인지확인
#토탈변수에 더하기
#토탈변수 출력

arr_2d = [list(map(int,input().split())) for _ in range(4)]
total=0
for i in range(4):
    for j in range(4):
        if j<=i:
            total+=arr_2d[i][j]
print(total) 