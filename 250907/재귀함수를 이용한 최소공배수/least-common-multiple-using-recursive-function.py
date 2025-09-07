n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
# 두 수가 주어졌을 떄 최대공약수 구하는 함수
def gcd(x, y):
    gcd=1
    for i in range(1, min(x,y)+1):
        if x%i==0 and y%i==0:
            gcd=i
    return gcd

# 두 수가 주어졌을 떄 최소공배수 구하는 함수
def lcm(x, y):
    #최소공배수 = 최대공약수 * 몫1 * 몫2
    return gcd(x,y) * (x//gcd(x,y)) * (y//gcd(x,y))

#arr에서 a번 인덱스의 원소까지의 최소공배수 구하는 재귀함수
def arr_lcm(a):
    #종료조건
    if a==0:
        return arr[0]
    
    #1, 2, 3, 4
    #일반화 : arr_lcm(3) = lcm(arr_lcm(2),arr[3])
    return lcm(arr_lcm(a-1), arr[a])

print(arr_lcm(n-1))
