a, b = map(int, input().split())

# Please write your code here.
# 매개변수 : a,b
# 큰수 += 25 / 작은수 *+ 2
def process(a,b):
    if a>b:
        a+=25
        b*=2
    else:
        b+=25
        a*=2
    return a,b

# 함수 호출 후
# 출력
a,b = process(a,b)
print(a,b)


