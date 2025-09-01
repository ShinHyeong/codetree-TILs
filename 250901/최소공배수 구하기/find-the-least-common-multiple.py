n, m = map(int, input().split())

# Please write your code here.

#함수 작성 - 매개변수:n,m /행위: 최소공배수출력
def lcm(n,m): #최대공약수 * n의 몫 * m의 몫
    #최대 공약수부터 구해본다
    gcd=1
    for i in range(1, min(n,m)+1):
        if n%i==0 and m%i==0:
            gcd=i
    #구했으면 n//gcd, m//gcd 도 구해주고
    #마지막엔 다 곱해서 출력한다
    print(gcd * (n//gcd) * (m//gcd))
#함수 실행
lcm(n,m)