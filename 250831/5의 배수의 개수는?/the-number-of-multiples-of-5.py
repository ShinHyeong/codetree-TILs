#4*4배열 입력받기
arr_2d = [list(map(int,input().split())) for _ in range(4)]
cnt=0

#배열을 돌면서
#5의배수 확인 -> 개수변수에 더하기
for i in range(4):
    for j in range(4):
        if arr_2d[i][j]%5==0:
            cnt+=1
#출력
print(cnt)
