n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 1x3 크기의 격자이므로
# 우측 방향으로 n-3 인덱스까지만 이동가능
max_val = 0
for i in range(n):
    for j in range(n-3+1):
        sum_val = grid[i][j] + grid[i][j+1] + grid[i][j+2]
        if sum_val > max_val:
            max_val = sum_val
print(max_val)