N = int(input())

# Please write your code here.
#재귀함수 1개만 사용
# n->1 : 1씩 감소하며 공백 두고 하나씩 출력
# 1->n : 1씩 증가하며 공백 두고 하나씩 출력
def print_digit(n):
    #종료조건 : n==0
    if n==0:
        return

    print(n,end=' ')
    print_digit(n-1)
    print(n,end=' ')

#함수실행
print_digit(N)