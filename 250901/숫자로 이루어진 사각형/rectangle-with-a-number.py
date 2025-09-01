# n을 입력받고
n = int(input())
# 함수 작성 - 매개변수 : n / 행위 : 일의 자리로 이루어진 정사각형 출력
def square(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    start = 1 #시작하는 수
    for i in range(n):
        for j in range(n):
            arr[i][j] = start
            print(arr[i][j],end=' ')
            start+=1
            if start%10==0: #일의 자리가 0이면 start를 1로 바꿔줌
                start = 1
        print()
# 함수 실행
square(n)