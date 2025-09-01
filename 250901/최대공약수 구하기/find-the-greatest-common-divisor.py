n, m = map(int, input().split())

# Please write your code here.
#함수 작성 - 매개변수 : 두 숫자, 행위 : 최대공약수 출력
def gcd(n,m): #최대공약수 : 두 수를 동시에 나눌 수 있는 가장 큰 수
#즉, n의 약수와 m의 약수 중 가장 큰 수
    gcd=1
    for i in range(1, min(n,m)+1):
        if n%i==0 and m%i==0:
            gcd = i
    print(gcd)
gcd(n,m)