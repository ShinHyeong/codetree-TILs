N = int(input())
pigeon = []
position = []
for _ in range(N):
    p, pos = map(int, input().split())
    pigeon.append(p)
    position.append(pos)

# Please write your code here.
# 비둘기 idx 별 현재위치를 기록하는 배열을 만든다
MIN_IDX, MAX_IDX = 1,10
first_pos = [-1] * (MAX_IDX+1)
ans = 0

# 비둘기 관찰 기록을 본다
# 처음위치랑 바뀌었을 경우 카운팅한다
for i in range(N):
    pigeon_idx = pigeon[i]

    #처음위치가 아닐 경우 기록하고 카운팅한다
    if first_pos[pigeon_idx] != -1 and position[i] != first_pos[pigeon_idx]:
        first_pos[pigeon_idx] = position[i]
        ans += 1

    #처음위치라면 기록한다
    if first_pos[pigeon_idx] == -1:
        first_pos[pigeon_idx] = position[i]

print(ans)
    