N = int(input())

# Please write your code here.
def fact(n):
    #종료조건 n==1
    if n==1: 
        return 1
    
    #일반화 : fact(10) = 10 * fact(9)
    return n * fact(n-1)

print(fact(N))