n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

# Please write your code here.
min_val, max_val = min(x1), max(x2)
arr = [0] * (max_val+1)

for i in range(n):
    for j in range(x1[i], x2[i]+1):
        arr[j]+=1

all_overlap = False
for a in arr:
    if a==n:
        all_overlap = True
        break

print("Yes" if all_overlap else "No")
    