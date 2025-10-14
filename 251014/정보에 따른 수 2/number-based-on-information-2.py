T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

# Please write your code here.
#특별한 위치인지
def is_special(k):
    d1,d2 = 1000, 1000
    for i in range(T):
        if c[i]=="S":
            d1 = min(abs(k-x[i]),d1)
        elif c[i]=="N":
            d2 = min(abs(k-x[i]),d2)

    if d1<=d2:
        return True

cnt=0
for i in range(a,b+1):
    if is_special(i):
        cnt+=1
print(cnt)