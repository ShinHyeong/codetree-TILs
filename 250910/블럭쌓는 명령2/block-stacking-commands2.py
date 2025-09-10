n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
# n개의 칸 (1번~n번)
blocks = [0] * (n+1)

#블록 쌓기
for c in commands:
    for i in range(c[0], c[1]+1):
        blocks[i] += 1

# 쌓은 블록 값 중 최댓값 출력
print(max(blocks[1:]))