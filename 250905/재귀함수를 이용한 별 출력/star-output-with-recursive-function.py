n = int(input())

# Please write your code here.
# 1~n줄까지 n개의 별 출력하는 재귀함수
def print_star(n):
    #종료조건 n==0
    if n==0:
        return 
    
    print_star(n-1)
    print("*" * n)

#함수 실행
print_star(n)