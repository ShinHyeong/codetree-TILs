n = int(input())

# Please write your code here.
# 매개변수 : n
# 2n개의 줄에 걸쳐서 별 출력
# n줄 : n->1개의 별 공백두고 출력
# n줄 : 1->n개의 별 공백두고 출력
def print_star(n):
    #종료조건 n==0
    if n==0:
        return
    
    print("* "*n)
    print_star(n-1)
    print("* "*n)

print_star(n)