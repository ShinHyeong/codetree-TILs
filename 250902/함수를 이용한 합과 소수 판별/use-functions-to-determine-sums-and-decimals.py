a, b = map(int, input().split())

# Please write your code here.
#조건1: 소수인지 검사하는 함수
def is_prime(x):
    for i in range(2,x): #2~x-1까지 나눠주면서 하나라도 나눠지면 소수가 아님
        if x%i==0:
            return False
    return True
#조건2: 모든 자릿수의 합이 짝수인지 검사
def isDigitSumEven(x):
    digitSum=0
    while x>0:
        digitSum += (x%10)
        x //= 10
    return digitSum%2==0

cnt=0
#a~b 돌면서
for x in range(a,b+1):
#조건1 + 조건2 충족하는지 확인
    if is_prime(x) and isDigitSumEven(x):
        cnt+=1
#개수변수 키우기
#개수변수 출력
print(cnt)