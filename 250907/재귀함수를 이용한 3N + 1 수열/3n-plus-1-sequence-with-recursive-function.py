n = int(input())

# Please write your code here.
# 1이 되기까지 몇 번 반복해야하는지 구하는 재귀함수
def f(n):
    #종료조건 n==1
    if n==1:
        return 0
    
    if n%2==0:
        n //= 2
    else:
        n = n3 + 1

    #일반화 : f(20)=f(10)+1
    return f(n)+1

# 1이 되기까지 몇 번 반복해야하는지 출력
print(f(n))