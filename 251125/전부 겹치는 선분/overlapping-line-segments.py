n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

# Please write your code here.

# min_x2 = 끝점에서의 가장 작은값
# max_x1 = 시작점에서의 가장 큰값
min_x2, max_x1 = min(x2), max(x1)

# max_x1 > min_x2 라면 절대 모든 선분이 겹칠 수 없다

print("Yes" if max_x1<=min_x2 else "No")