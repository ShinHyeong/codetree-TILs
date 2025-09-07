N = int(input())

# Please write your code here.
# n==홀수 : 1~n까지의 홀수 합
# n==짝수 : 2~n까지의 짝수 합 
def get_sum(n):
    #2씩 줄어들며
    #마지막 수일 경우 종료 (짝수:2, 홀수:1)
    if n==2:
        return 2
    if n==1:
        return 1
        
    #일반화: get_sum(12) = 12 + get_sum(10)
    return n+get_sum(n-2)
    
print(get_sum(N))