N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
def process(t, ta, tb):
    if t<ta:
        return C
    elif ta<=t and t<=tb:
        return G
    elif t>=tb:
        return H

max_val = 0
for t in range(1001): #적정 온도
    sum_val = 0
    for ta, tb in ranges:
        sum_val += process(t, ta, tb)
    max_val = max(sum_val, max_val)
print(max_val)