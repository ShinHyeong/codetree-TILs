n = int(input())

# Please write your code here.
# 재귀함수 작성 : "HelloWorld"를 n번 출력하는 함수
def print_text(n):
    #종료조건 n==0 / 동작종료
    if n==0:
        return
    
    print_text(n-1)
    print("HelloWorld")

print_text(n)