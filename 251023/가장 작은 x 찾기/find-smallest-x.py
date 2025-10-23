n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

# Please write your code here.
for x_val in range(1,10000):
    x = x_val
    answer = True
    for i in range(n):
        x *= 2
        if a[i]>x or x>b[i]: 
            answer = False #한번이라도 a이상b이하면 탈락
    if answer==True:
        print(x_val)
        break
