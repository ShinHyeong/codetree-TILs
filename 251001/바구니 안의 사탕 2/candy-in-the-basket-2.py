N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.

#바구니 안에 사탕 넣기
baskets = [0] * 101 #0 ~ 100
for i in range(len(pos)):
    position = pos[i]
    baskets[position] = candy[i]

#중심점을 잘 잡아 구간에 있는 사탕수가 최대인지 확인후 출력
max_val = 0
for c in range(len(baskets)):
    sum_val = sum(baskets[c-K:c+K+1])
    max_val = max(sum_val, max_val)
print(max_val)