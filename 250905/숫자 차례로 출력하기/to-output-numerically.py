n = int(input())

# Please write your code here.
# 재귀함수1 : 1->N 숫자 차례로 공백을 사이에 두고 출력
# 매개변수 : n
def print_asc(n):
    #종료조건 n==0
    if n==0:
        return

    print_asc(n-1)
    print(n,end=' ')

# 재귀함수2 : N->1 숫자 차례로 공백을 사이에 두고 출력 
# 매개변수 n
def print_dsc(n):
    #종료조건 n==0
    if n==0:
        return
    
    print(n, end=' ')
    print_dsc(n-1)

#함수실행
print_asc(n)
print()
print_dsc(n)