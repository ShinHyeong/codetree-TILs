a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
#각 사칙연산에 해당하는 4개의 함수 작성
def add(a,b):
    return a+b
def sub(a,b):
    return a-b if a>b else b-a
def multi(a,b):
    return a*b
def divide(a,b):
    return a//b if a>b else b//a

#매개변수 : 정수와 연산식
#조건 -> 적절한 함수 골라줌
if o=='+':
    print(f"{a} + {c} = {add(a,c)}")
elif o=='-':
    print(f"{a} - {c} = {sub(a,c)}")
elif o=='*':
    print(f"{a} * {c} = {multi(a,c)}")
elif o=="/":
    print(f"{a} / {c} = {divide(a,c)}")
else:
    print("False")
#그 결과 출력