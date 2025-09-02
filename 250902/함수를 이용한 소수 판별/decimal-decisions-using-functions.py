a, b = map(int, input().split())

# Please write your code here.
#소수인지 검사하는 함수 : 2~(x-1)까지 나눠주면서 하나라도 나눠지면 그건 소수가 아님
def is_prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

total=0
for x in range(a,b+1): #a~b까지 돌면서
    if is_prime(x): #소수인지 검사
        total += x #소수라면 토탈변수에 더하자

print(total) #토탈변수 출력