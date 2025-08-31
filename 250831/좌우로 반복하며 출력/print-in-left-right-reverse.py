#정사각형의 크기 입력받기
#0으로 된 정사각형 만들기
n=int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

#배열 돌고
for i in range(n):
    start=1 #각 행마다 start는 1로 초기화
    #짝수행인지 검사 : 짝수면 순서대로, 홀수면 역방향으로 채우기
    if i%2==0:
        for j in range(n):
            arr[i][j]=start
            start+=1
    else:
        for j in range(n-1,-1,-1):
            arr[i][j]=start
            start+=1

#배열 쭉 돌면서 출력
for i in range(n):
    for j in range(n):
        print(arr[i][j],end="")
    print()