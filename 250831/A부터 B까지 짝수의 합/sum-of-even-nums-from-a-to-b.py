#정수 a,b 입력받기
#a~b까지 돌면서
#짝수면 합변수에 더하기
#합변수출력

a,b=tuple(map(int,input().split()))
total=0
for i in range(a,b+1):
    if i%2==0:
        total+=i
print(total)