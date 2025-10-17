A, B, C = map(int, input().split())

# Please write your code here.
max_val = 0
for i in range(1000):
    for j in range(1000):
        if (A*i) + (B*j) <= C:
            max_val = max(max_val, (A*i)+(B*j))
print(max_val)