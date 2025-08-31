#n번에 걸쳐서
#두 정수 입력받기
#a~b까지 돌면서
#짝수인지 검사하고
#맞다면 더해서
#각 줄마다 출력

n=int(input())

for _ in range(n):
    total=0
    a,b=tuple(map(int,input().split()))
    for i in range(a,b+1):
        if i%2==0:
            total+=i
    print(total)