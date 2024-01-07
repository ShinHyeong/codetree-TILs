def 더하기(a,c):
    return a+c
def 나누기(a,c):
    return a//c
def 빼기(a,c):
    return max(a,c)-min(a,c)
def 곱하기(a,c):
    return a*c

a,o,b = input().split()
a=int(a)
b=int(b)
if o=="+":
    print(f"{a} {o} {b} = {더하기(a,b)}")
elif o=="-":
    print(f"{a} {o} {b} = {빼기(a,b)}")
elif o=="/":
    print(f"{a} {o} {b} = {나누기(a,b)}")
else:
    print(f"{a} {o} {b} = {곱하기(a,b)}")