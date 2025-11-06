N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.

#idx의 차(거리) <= k
    #터진다
#N크기의 폭탄리스트를 만들고 터진 갯수를 저장한다
#가장 많이 터진 폭탄의 번호를 출력한다

bomb = [False] * N

for i in range(N):
    for j in range(i+1,N):
        if (j-i)<=K:
            bomb[i],bomb[j] = True,True

MAX_NUM = max(num)
bomb_cnt = [0] * (MAX_NUM+1)
for pos in range(N):
    if bomb[pos]:
        n = num[pos] #해당 위치의 폭탄 숫자를 넘겨주고
        bomb_cnt[n] += 1 #그 숫자 갯수를 센다

max_bomb_i = bomb_cnt.index(min(bomb_cnt))
for i,cnt in enumerate(bomb_cnt):
    if cnt == max(bomb_cnt):
        max_bomb_i = max(max_bomb_i, i)
print(max_bomb_i)