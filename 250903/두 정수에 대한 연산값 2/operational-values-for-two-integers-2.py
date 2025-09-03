a, b = map(int, input().split())

# Please write your code here.
# 매개변수 : a,b
# 큰수 *= 2 / 작은수 +=10
def process(a,b):
    if a>b:
        a*=2
        b+=10
    else:
        b*=2
        a+=10
    return a,b

# 함수 호출 후
# 출력
a,b = process(a,b)
print(a,b)



